import datetime
import os
from pathlib import Path

from google.adk.agents import Agent
from google.adk.agents.readonly_context import ReadonlyContext
from google.adk.apps import App
from google.adk.environment import LocalEnvironment
from google.adk.models import Gemini
from google.adk.skills import load_skill_from_dir
from google.adk.tools.environment import EnvironmentToolset
from google.adk.tools.skill_toolset import SkillToolset
from google.genai import types

MODEL = os.getenv("MODEL", "gemini-flash-lite-latest")

CURRENT_DIR = Path(__file__).resolve().parent
SKILLS_PLANO_DIR = CURRENT_DIR / "skills" / "plano-de-estudos"
SKILLS_REVISAO_DIR = CURRENT_DIR / "skills" / "revisao-ativa"
PLANOS_DIR = CURRENT_DIR.parent / "planos"
PLANOS_DIR.mkdir(parents=True, exist_ok=True)


class FerramentasDeArquivo(EnvironmentToolset):
    """Subclasse de EnvironmentToolset que expõe apenas ReadFile e WriteFile."""

    async def get_tools(self, readonly_context=None):
        tools = await super().get_tools(readonly_context)
        return [t for t in tools if t.name in ("ReadFile", "WriteFile")]


def instruction_provider(context: ReadonlyContext | None = None) -> str:
    hoje = datetime.date.today().strftime("%d/%m/%Y")
    dia_semana = datetime.date.today().strftime("%A")
    dias_semana_pt = {
        "Monday": "segunda-feira",
        "Tuesday": "terça-feira",
        "Wednesday": "quarta-feira",
        "Thursday": "quinta-feira",
        "Friday": "sexta-feira",
        "Saturday": "sábado",
        "Sunday": "domingo",
    }
    dia_pt = dias_semana_pt.get(dia_semana, dia_semana)
    return (
        f"Hoje é {dia_pt}, dia {hoje}.\n"
        "Você é um mentor de estudos especializado em criar planos de estudo personalizados e em gerar materiais de revisão ativa (flashcards e quizzes).\n"
        "Você utiliza as skills 'plano-de-estudos' e 'revisao-ativa'. Siga rigorosamente as instruções da skill acionada e a regra de ativação (gating rule) antes de avançar para os passos seguintes."
    )


root_agent = Agent(
    name="agente_estudos",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=instruction_provider,
    tools=[
        SkillToolset(
            skills=[
                load_skill_from_dir(SKILLS_PLANO_DIR),
                load_skill_from_dir(SKILLS_REVISAO_DIR),
            ]
        ),
        FerramentasDeArquivo(
            environment=LocalEnvironment(working_dir=str(PLANOS_DIR))
        ),
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)
