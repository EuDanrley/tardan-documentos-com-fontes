# Como montar o assistente (escolha um caminho)

Todos os caminhos usam a mesma instrução (`instrucao-pronta.md`) e os seus documentos. Informações sobre planos e limites conferidas nas páginas oficiais em **02/11/2026**. Planos mudam: confira na tela antes de assinar qualquer coisa.

| Caminho | Bom para | Custo para começar |
|---|---|---|
| A. Projeto do Claude | Equipe pequena que já usa Claude | Plano gratuito tem Projetos (até 5) |
| B. Projeto do ChatGPT | Quem já usa ChatGPT | Plano gratuito tem Projetos (até 5 arquivos por projeto) |
| C. Gemini Notebook (ex-NotebookLM) | Muitos documentos e respostas com citação clicável | Plano Standard: até 50 fontes por caderno |
| D. Local / open source | Documentos que não podem sair do computador | Software gratuito; exige computador com capacidade suficiente e alguém para instalar |

> Antes de subir qualquer arquivo: tire dados pessoais de clientes e funcionários que a consulta não precisa (CPF, telefone, endereço, salário, saúde). Veja o aviso de privacidade no fim deste arquivo.

---

## A. Projeto do Claude (claude.ai)

1. Entre em claude.ai e clique em **Projects** (Projetos) na barra lateral → **New project** (Novo projeto). Dê um nome, ex.: "Consulta aos documentos".
2. Em **Instructions** (Instruções do projeto), cole o bloco "Instrução completa" de `instrucao-pronta.md`. Troque `[NOME DA EMPRESA]`.
3. Em **Project knowledge** (Conhecimento do projeto), envie seus documentos (.docx, .pdf com texto, .md ou .txt). Para testar, envie os arquivos de `exemplos/entrada-ficticia/` ou `exemplos/entrada-ficticia/docx/`.
4. Abra uma conversa dentro do projeto e faça as perguntas de `exemplos/perguntas-de-teste.md`, uma por vez. Compare com `exemplos/saida-esperada.md`.

O que a página oficial diz (support.claude.com/en/articles/9519177, consultada em 02/11/2026):
- Projetos estão disponíveis também no plano gratuito; usuários gratuitos podem criar **no máximo 5 projetos**.
- O conteúdo enviado ao conhecimento do projeto vale para todas as conversas daquele projeto.
- Em planos **pagos**, quando o conhecimento se aproxima do limite de contexto, o Claude ativa automaticamente um modo de busca (RAG) para ampliar a capacidade. A página não diz que isso existe no plano gratuito.
- A página **não informa** limite de quantidade ou tamanho de arquivos.

## B. Projeto do ChatGPT (chatgpt.com)

1. Na barra lateral, clique em **Projetos** → **Novo projeto**.
2. Abra as configurações do projeto e cole a "Instrução completa" no campo de **instruções**. As instruções do projeto valem só dentro dele e passam por cima das suas instruções personalizadas gerais.
3. Adicione os arquivos ao projeto.
4. Teste com as perguntas de exemplo, uma por vez.

O que a Central de Ajuda da OpenAI diz (help.openai.com/en/articles/10169521; a página bloqueou a leitura direta com erro 403 em 02/11/2026, então conferimos pelo conteúdo indexado da própria Central — confirme na sua conta):
- Free: até **5 arquivos por projeto** e limite de **3 uploads por dia**.
- Go e Plus: até 25 arquivos por projeto. Edu, Pro, Business e Enterprise: até 40.
- Free, Plus e Pro: informações acessadas em projetos podem ser usadas para treinar modelos se a opção "Improve the model for everyone" (Melhorar o modelo para todos) estiver ligada.

**Por que não usamos GPT personalizado:** pela Central de Ajuda da OpenAI (help.openai.com/en/articles/20001519, mesma ressalva de leitura), contas pessoais (Free, Go, Plus e Pro) não podem mais criar GPTs novos, e os GPTs personalizados têm aposentadoria prevista para 11/12/2026, com migração para plugins. Por isso este módulo usa Projetos.

## C. Gemini Notebook (antigo NotebookLM)

O Google renomeou o NotebookLM para **Gemini Notebook** em 16/07/2026 (blog.google). No anúncio, o link para usar continua sendo notebooklm.google; os cadernos também aparecem no app Gemini.

1. Acesse notebooklm.google e crie um caderno.
2. Adicione os documentos como fontes.
3. Em **Configurações** (canto superior direito) → **Idioma de saída** (Output Language), escolha **Português (Brasil)**.
4. Se a sua conta mostrar a opção de personalizar o chat (objetivo ou estilo da conversa), cole a **Versão curta** de `instrucao-pronta.md`. Se não mostrar, cole a versão curta como primeira mensagem do chat. *A existência dessa opção na versão atual não foi conferida nesta produção.*
5. Faça as perguntas de teste. As respostas trazem referências às fontes; clique para conferir o trecho.

O que as páginas oficiais dizem (consultadas em 02/11/2026):
- Tabela "Usage Limits (Subject to Change)" (support.google.com/notebooklm/answer/16213268): Standard — 100 cadernos e **50 fontes por caderno**; Plus — 200 e 100; Pro — 500 e 300; Ultra (20 TB) — 500 e 500; Ultra (30 TB) — 500 e 600.
- Cada fonte: até 500 mil palavras ou 200 MB em upload local, sem limite de páginas. PDF protegido contra cópia falha na importação (FAQ, answer/16269187).
- Se a fonte for curta demais, a ferramenta referencia o documento inteiro, e a resposta pode não citar trechos específicos. Por isso vale numerar seções.
- Português (Brasil) está na lista de idiomas de saída (support.google.com/gemininotebook/answer/16261963).
- Países: a FAQ remete à lista de regiões do app Gemini; o Brasil está nessa lista (support.google.com/gemini/answer/13575153).
- Preço dos planos Google AI em reais: **não confirmado** nesta produção.
- Uso dos seus dados para treinar modelos: a FAQ diz "Seus dados nunca serão compartilhados pelo Gemini Notebook", mas não trata de treino. **Não confirmado.**

**Por que não usamos Gem:** pela Central de Ajuda do Gemini (support.google.com/gemini/answer/18560919), em contas pessoais os Gems ficam somente leitura em 17/11/2026 e são removidos em 17/12/2026, substituídos por Skills.

## D. Local / open source

Veja a aula 3 e o `README.md` (seção "Caminho local"). Resumo: **AnythingLLM Desktop** (licença MIT) ou **Open WebUI + Ollama** (Open WebUI tem licença própria com regra de marca; Ollama é MIT). Exigem instalação e um computador com memória suficiente para o modelo escolhido.

---

## Bônus: a mesma instrução como Skill (Claude ou Gemini)

A pasta `claude-skill/documentos-com-fontes/` contém um `SKILL.md`. Ela ajuda quando você quer o mesmo comportamento numa conversa comum, anexando os documentos na hora. Para consulta diária, prefira o Projeto ou o Gemini Notebook, porque lá os documentos ficam guardados.

**No Claude** (support.claude.com/en/articles/12512180 e 12512198, consultados em 02/11/2026; disponível nos planos Free, Pro, Max, Ultra, Team e Enterprise):
1. Ligue **Settings → Capabilities → Code execution and file creation** (na tela nova: "Create and edit files").
2. Compacte a **pasta** `documentos-com-fontes` em ZIP (a pasta fica na raiz do ZIP, não os arquivos soltos).
3. **Customize → Skills → + → Create skill → Upload a skill** e envie o ZIP.

**No Gemini** (support.google.com/gemini/answer/17094296, consultado em 02/11/2026; "disponível sem assinatura Google AI"; exige 18 anos ou mais e Atividade/Keep Activity ligada):
1. Em gemini.google.com: **Customize → Skills → Create → Upload**.
2. Selecione o `SKILL.md` ou a pasta. Limite de 100 MB no total dos arquivos.

---

## Privacidade e LGPD (aviso, não parecer jurídico)

- Documentos de regra geral (políticas, prazos, manuais) normalmente não precisam de dados pessoais. Tire o que não for necessário antes de subir.
- Não suba cadastro de clientes, folha de pagamento, atestados ou conversas com clientes sem avaliar a base legal e a necessidade com quem cuida de dados na sua empresa.
- Confira as opções de privacidade da ferramenta. No Claude: Configurações → Privacidade, opção de permitir o uso dos chats para melhorar os modelos (planos Free, Pro e Max); chats anônimos (incognito) não são usados para treino (privacy.claude.com/en/articles/12109829). No ChatGPT: opção "Improve the model for everyone".
- Lei Geral de Proteção de Dados: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · ANPD: https://www.gov.br/anpd/
