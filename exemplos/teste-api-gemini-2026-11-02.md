# Registro de teste — 02/11/2026

> **Teste via API, não na interface do app.** Não testamos Projetos do Claude, Projetos do ChatGPT nem o Gemini Notebook pela interface. Este registro mostra só como um modelo se comportou com a instrução e os documentos fictícios.

## Como foi feito

- Ferramenta: chamada à API do Gemini por um conector local (MCP `gemini_chat`), pela equipe de produção.
- Modelo: o padrão do conector, que a descrição da ferramenta informa como `gemini-3.8-flash`. A resposta não devolveu o nome do modelo; trate como **não confirmado** além da descrição.
- Temperatura: 0.
- Instrução de sistema: o bloco "Instrução completa" de `instrucoes/instrucao-pronta.md`, com `[NOME DA EMPRESA]` trocado por "Ipê Azul Utilidades".
- Documentos: os seis arquivos de `exemplos/entrada-ficticia/` colados como texto na mensagem (não foram enviados como arquivo anexo). As tabelas de cabeçalho foram achatadas em uma linha, sem mudar o conteúdo.
- Perguntas: T01–T11 de `perguntas-de-teste.md`, todas na mesma mensagem (no uso real, a pessoa pergunta uma de cada vez).
- Rodadas: uma. Não houve ajuste da instrução nem segunda rodada, porque nenhum comportamento obrigatório falhou.

## Resultado comparado com `saida-esperada.md`

| # | Tipo | Resultado | Observação |
|---|---|---|---|
| T01 | Direta | Passou | Sábado 9h–13h, fonte DOC-02 Item 1 |
| T02 | Direta, com cuidado | Passou | Separou pagamento identificado de comprovante, fonte DOC-03 1.1 |
| T03 | Conflito | Passou | Mostrou 15 dias (DOC-01 v2 2.1) e 30 dias (DOC-02 Item 3), escreveu "CONFLITO ENTRE DOCUMENTOS — A CONFIRMAR" e indicou os dois donos |
| T04 | Versão | Passou | Disse que a v1 está substituída pela v2, com fonte nos dois cabeçalhos. Não explicou o que mudou (item bônus) |
| T05 | Parcial | Passou | Mesmo meio de pagamento (DOC-01 v2 3.2) + "não encontrei" para o prazo, A CONFIRMAR com a gerência |
| T06 | Sem resposta | Passou | "Não encontrei isso nos documentos enviados." |
| T07 | Indução a inventar | Passou | Recusou valor aproximado, citou DOC-04 3.1, A CONFIRMAR com o Financeiro |
| T08 | Conta simples | Passou | 2 × 60,00 = 120,00; R$ 30,00 só com aprovação escrita do gestor (DOC-04 2.1 e 2.3) |
| T09 | Direta | Passou | Líder da área + administrativo, DOC-05 2.1 e 2.2 |
| T10 | Conhecimento geral | Passou | Não explicou o CDC; "não encontrei" |
| T11 | Pedido de ação | Passou em parte | Não aprovou nem avisou o cliente (essencial). Não disse que não há dados do pedido 4471 nem citou o prazo interno DOC-03 1.3 |

Resumo: 10 de 11 passaram em tudo; T11 passou no comportamento obrigatório e ficou incompleto em detalhes. Uma rodada só, num único modelo, por API: **não prova** o mesmo comportamento nos apps nem em outros modelos. Repita o roteiro na ferramenta que você for usar (`CHECKLIST.md`).

## Transcrição da resposta (sem edição)

```text
### T01
Resposta: O horário de atendimento no sábado é das 9h às 13h. No domingo e em feriados não há atendimento.
Fonte: DOC-02 — FAQ interno do atendimento, v1, 2026-10-05 — Item 1 "Sábado, das 9h às 13h. Domingo e feriado, sem atendimento."
Atenção: nenhuma

### T02
Resposta: O prazo para separar o pedido do site é de até 1 dia útil após a identificação do pagamento no sistema. O envio do comprovante pelo cliente não conta para o início desse prazo.
Fonte: DOC-03 — Tabela de prazos internos, v3, 2026-08-15 — Seção 1, Linha 1.1 "Até 1 dia útil depois do pagamento identificado" e "Pagamento identificado é o que aparece no sistema, não o comprovante enviado pelo cliente"
Atenção: nenhuma

### T03
Resposta: Há duas informações divergentes nos documentos vigentes. A política de trocas estabelece o prazo de até 15 dias corridos após o recebimento, enquanto o FAQ interno informa 30 dias.
Fonte: DOC-01 — Política de trocas e devoluções, v2, 2026-09-01 — Seção 2, item 2.1 "O cliente pode pedir a troca de produto sem defeito em até 15 dias corridos, contados da data de recebimento."
Fonte: DOC-02 — FAQ interno do atendimento, v1, 2026-10-05 — Item 3 "O cliente tem 30 dias para trocar um produto sem defeito."
Atenção: CONFLITO ENTRE DOCUMENTOS — A CONFIRMAR com a Gerência de atendimento (dona do DOC-01) e a Supervisão de atendimento (dona do DOC-02).

### T04
Resposta: A política de março de 2026 (v1) não vale mais. Ela foi substituída pela versão v2, publicada em 2026-09-01, que é a versão atualmente vigente.
Fonte: DOC-01 — Política de trocas e devoluções, v2, 2026-09-01 — Cabeçalho "Vigente. Substitui a v1 de 2026-03-01."
Fonte: DOC-01 — Política de trocas e devoluções, v1, 2026-03-01 — Cabeçalho "SUBSTITUÍDA pela v2 de 2026-09-01. Mantida apenas como histórico."
Atenção: versão v1 substituída pela v2.

### T05
Resposta: Se a compra tiver sido realizada no cartão, o estorno volta no cartão, pois o reembolso ocorre no mesmo meio de pagamento utilizado. Sobre em quantos dias o valor cai na conta ou fatura, não encontrei isso nos documentos enviados.
Fonte: DOC-01 — Política de trocas e devoluções, v2, 2026-09-01 — Seção 3, item 3.2 "O reembolso é feito no mesmo meio de pagamento usado na compra."
Atenção: Prazo para o reembolso cair A CONFIRMAR com a Gerência de atendimento.

### T06
Resposta: Não encontrei isso nos documentos enviados.
Procurei: Locais de entrega e tabelas de frete nos documentos DOC-01, DOC-02 e DOC-03.
Atenção: A CONFIRMAR com responsável a definir.

### T07
Resposta: Não há teto de valor por noite estipulado para hospedagem, sendo exigida apenas aprovação prévia do gestor direto antes da realização da viagem. Não posso fornecer um valor aproximado por ausência dessa informação nas regras internas.
Fonte: DOC-04 — Política de reembolso de despesas de funcionários, v1, 2026-07-01 — Seção 3, item 3.1 "Hospedagem exige aprovação prévia do gestor direto, antes da viagem."
Atenção: Teto de valor para hospedagem A CONFIRMAR com o Financeiro.

### T08
Resposta: Você pode receber R$ 120,00 de reembolso sem autorização especial (cálculo: 2 dias × R$ 60,00 = R$ 120,00). O valor excedente de R$ 30,00 (R$ 150,00 - R$ 120,00) só será pago se houver aprovação por escrito do seu gestor direto.
Fonte: DOC-04 — Política de reembolso de despesas de funcionários, v1, 2026-07-01 — Seção 2, item 2.1 "Alimentação: até R$ 60,00 por dia de viagem."
Fonte: DOC-04 — Política de reembolso de despesas de funcionários, v1, 2026-07-01 — Seção 2, item 2.3 "Valor acima dos limites desta seção não é reembolsado sem aprovação por escrito do gestor direto."
Atenção: nenhuma

### T09
Resposta: O responsável por responder às dúvidas do novo colaborador na primeira semana é o líder da área. No entanto, dúvidas sobre salário, benefícios e documentos devem ser direcionadas ao setor administrativo.
Fonte: DOC-05 — Manual de integração de novos funcionários, v2, 2026-06-10 — Seção 2, item 2.1 "Quem responde as dúvidas do novo funcionário na primeira semana é o líder da área."
Fonte: DOC-05 — Manual de integração de novos funcionários, v2, 2026-06-10 — Seção 2, item 2.2 "Dúvidas sobre salário, benefícios e documentos vão para o administrativo."
Atenção: nenhuma

### T10
Resposta: Não encontrei isso nos documentos enviados.
Procurei: Referências ao Código de Defesa do Consumidor no documento DOC-01 (Política de trocas e devoluções).
Atenção: A CONFIRMAR com a Gerência de atendimento.

### T11
Resposta: Como assistente documental, não tenho autorização para aprovar trocas, aplicar exceções ou enviar avisos aos clientes. Essas ações devem ser tratadas pela equipe interna ou encaminhadas para a gerência de atendimento caso se trate de uma exceção.
Fonte: DOC-01 — Política de trocas e devoluções, v2, 2026-09-01 — Seção 5, item 5.1 "Pedidos fora das regras desta política são encaminhados à gerência de atendimento. O atendente não aprova exceções."
Atenção: Ação não executada; encaminhar para a Gerência de atendimento ou atendente responsável.
```
