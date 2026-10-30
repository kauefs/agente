import pytest
from pathlib import Path
from google.adk.environment import LocalEnvironment
from app.agent import FerramentasDeArquivo, root_agent


@pytest.mark.asyncio
async def test_ferramentas_de_arquivo_filtro(tmp_path: Path) -> None:
    toolset = FerramentasDeArquivo(
        environment=LocalEnvironment(working_dir=str(tmp_path))
    )
    tools = await toolset.get_tools()
    tool_names = [t.name for t in tools]
    
    assert set(tool_names) == {"ReadFile", "WriteFile"}
    assert "Execute" not in tool_names
    assert "EditFile" not in tool_names


def test_agent_skills_carregadas() -> None:
    assert root_agent.name == "agente_estudos"
    # Garante que as duas ferramentas de skill (SkillToolset) foram adicionadas
    assert len(root_agent.tools) == 2
