# tardan-documentos-com-fontes

Um assistente que responde perguntas da sua equipe **só com base nos documentos da sua empresa**, dizendo de qual documento, versão e item tirou a resposta, e que diz "Não encontrei isso nos documentos enviados" quando a resposta não está lá.

## Use em 5 minutos

1. **Baixe:** botão verde **Code → Download ZIP**. Descompacte a pasta.
2. **Crie o assistente:** no Claude ou no ChatGPT, crie um **Projeto** e cole no campo de instruções o bloco "Instrução completa" de `instrucoes/instrucao-pronta.md`. (Prefere o Gemini Notebook? Siga o caminho C de `instrucoes/projeto-ia.md`.)
3. **Teste com a empresa fictícia:** envie ao projeto os arquivos de `exemplos/entrada-ficticia/docx/` e faça 3 perguntas de `exemplos/perguntas-de-teste.md`: T01 (direta), T03 (conflito) e T06 (sem resposta). Compare com `exemplos/saida-esperada.md`.
4. **Troque pelos seus documentos:** apague os fictícios do projeto, coloque o cabeçalho de `modelos/ficha-de-documento.docx` no topo de cada documento seu (código, versão, data, dono, estado) e envie.
5. **Confira antes de liberar:** rode 8 a 12 perguntas reais com o `CHECKLIST.md`. Só libere para a equipe quando o "não encontrei" e os conflitos aparecerem certo.

## O que você precisa

- Uma conta em **Claude**, **ChatGPT** ou **Google** (Gemini Notebook). Os planos gratuitos têm limites; os números conferidos em 02/11/2026 estão em `instrucoes/projeto-ia.md`:
  - Claude grátis: até 5 projetos.
  - ChatGPT grátis: até 5 arquivos por projeto e 3 uploads por dia.
  - Gemini Notebook (plano Standard): até 50 fontes por caderno.
- Seus documentos em .docx, .pdf com texto selecionável, .txt ou .md, **sem dados pessoais desnecessários**.
- Para o caminho local (opcional): computador com memória suficiente para rodar um modelo de IA e alguém disposto a instalar programas.

## Arquivos do repositório

| Caminho | Para que serve |
|---|---|
| `instrucoes/instrucao-pronta.md` | Instrução para colar (versão completa e versão curta) |
| `instrucoes/projeto-ia.md` | Passo a passo: Projeto do Claude, Projeto do ChatGPT, Gemini Notebook, Skill; limites e privacidade |
| `instrucoes/claude-skill/documentos-com-fontes/SKILL.md` | A mesma instrução como Skill (Claude ou Gemini) |
| `modelos/ficha-de-documento.md` e `.docx` | Cabeçalho para colocar em cada documento |
| `modelos/modelo-resposta-com-citacao.md` | Os três formatos de resposta e como conferir em 30 s |
| `modelos/roteiro-de-organizacao.md` | Como separar e preparar os documentos antes de subir |
| `modelos/indice-de-documentos.csv` | Lista dos documentos do assistente, com versão e dono |
| `modelos/roteiro-de-testes-modelo.csv` | Planilha para testar com perguntas da sua equipe |
| `exemplos/entrada-ficticia/` | 6 documentos de uma empresa **fictícia** (.md e .docx), com um conflito e lacunas de propósito |
| `exemplos/perguntas-de-teste.md` e `roteiro-de-testes-ficticio.csv` | 11 perguntas de teste |
| `exemplos/saida-esperada.md` | Gabarito: resposta, fonte e comportamento esperados |
| `exemplos/teste-api-gemini-2026-11-02.md` | Registro de um teste feito por API (não na interface dos apps) |
| `scripts/` | Opcional: converte .md em .docx (testado; veja `scripts/LEIA-ME.md`) |
| `CHECKLIST.md` | Conferência antes de usar as respostas |

## Caminho local (opcional)

Para documentos que não podem sair do computador. Licenças conferidas nas fontes oficiais em 02/11/2026:

- **AnythingLLM Desktop** — licença MIT (Mintplex Labs Inc.). Gratuito, sem cadastro, para Windows, macOS e Linux. Traz um mecanismo local de modelos embutido e também funciona com Ollama; mostra citações das fontes. https://anythingllm.com/desktop · https://github.com/Mintplex-Labs/anything-llm
- **Open WebUI + Ollama** — Open WebUI usa hoje a **Open WebUI License** (não é mais MIT/BSD puro): permite usar e redistribuir mantendo os avisos, mas proíbe alterar ou remover a marca "Open WebUI", exceto em implantações com até 50 usuários finais em 30 dias, com autorização escrita ou licença enterprise. Ollama é MIT. https://github.com/open-webui/open-webui · https://ollama.com

Detalhes, comandos e limites na aula 3 do módulo.

## Quer entender ou adaptar?

As aulas do módulo 06 do Pro mostram o assistente funcionando (aula 1), como adaptar aos seus documentos e casos difíceis (aula 2) e como funciona por dentro, com a opção local (aula 3). Prefere que a equipe Tardan monte para a sua empresa? Use o botão **"Quero que façam para mim"** e combine escopo e proposta pelo WhatsApp. Esse serviço não está incluído no Pro.

## Limites

- O assistente pode errar: ler mal uma tabela, citar o item errado ou perder um trecho em documentos longos. Confira a fonte antes de usar uma resposta com cliente, dinheiro ou funcionário.
- Ele só sabe o que está nos documentos enviados. Documento desatualizado gera resposta desatualizada.
- Não substitui orientação jurídica, contábil ou trabalhista.
- Não executa ações (não aprova, não envia, não altera nada).
- Os limites de planos citados mudam; confira na tela da ferramenta.

## Licença

Veja `LICENCA.md`. Material da Comunidade Tardan para membros ativos. Projetos de terceiros citados mantêm suas próprias licenças.
