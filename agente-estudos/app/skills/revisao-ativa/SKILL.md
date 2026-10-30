---
name: revisao-ativa
description: Gera flashcards e um quiz de 5 perguntas com gabarito a partir de um material de estudo, nota de aula ou tópico. Use quando a pessoa quiser praticar recuperação ativa, testar seus conhecimentos ou criar material de revisão.
---

# [IMPORTANTE] UTILIZAR ESTA SKILL PARA REVISÃO ATIVA E TESTES

Esta skill transforma um material de estudo (texto, notas, código, transcrição ou tópico) em **ferramentas de recuperação ativa**: um conjunto de **flashcards** (frente e verso) e um **quiz de 5 perguntas** com gabarito explicativo.

## Regra de Ativação (Gating Rule)

Verifique se a conversa já contém o **material ou tópico de estudo**:

| # | Informação obrigatória | Exemplo |
|---|---|---|
| 1 | **Material ou Tópico de Estudo**: texto, resumo, notas de aula, código ou assunto específico | "Quero revisar o conceito de closures em JavaScript: [texto/código]" ou "Quero um quiz sobre Python básico" |

* **Se faltar o material/tópico:** **NÃO chame** a ferramenta `load_skill_resource` e não carregue nenhum arquivo de `references/` ou `assets/`. Faça **uma única mensagem**, curta e amigável, pedindo o texto, resumo ou tópico que a pessoa deseja revisar.
* **Se o material/tópico estiver presente:** prossiga imediatamente para as instruções abaixo.

## Instruções (apenas depois que o gating for satisfeito)

1. Use a ferramenta `load_skill_resource` para ler `references/workflow.md`.
2. Siga **estritamente** os passos descritos em `references/workflow.md`. Ele indica o momento correto de carregar `assets/revisao_template.md`.
3. Se for a primeira revisão da conversa, consulte `assets/exemplo_revisao.md` para calibrar o nível de detalhe esperado.

## Regras gerais

* Responda sempre em **português do Brasil**, num tom didático, direto e encorajador.
* Os **flashcards** devem focar em conceitos-chave, definições, comparações e 'por quês', promovendo recuperação ativa.
* O **quiz de 5 perguntas** deve ser variado (questões conceituais e práticas) acompanhadas de um **gabarito comentado**.
