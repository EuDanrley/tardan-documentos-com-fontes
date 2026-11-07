# Checklist — antes de liberar e antes de usar uma resposta

## Antes de liberar o assistente para a equipe

- [ ] Só documentos aprovados; rascunhos fora ou marcados "não usar".
- [ ] Cada documento tem cabeçalho: código, versão, data, dono, estado.
- [ ] Versões antigas removidas ou marcadas "SUBSTITUÍDA".
- [ ] Seções e itens numerados (1.1, 1.2…).
- [ ] Dados pessoais desnecessários removidos (CPF, telefone, endereço, salário, saúde).
- [ ] Opção de uso dos dados para treino conferida na ferramenta.
- [ ] Rodei 8 a 12 perguntas reais em `roteiro-de-testes-modelo.csv`, incluindo:
  - [ ] uma sem resposta nos documentos → respondeu "Não encontrei isso nos documentos enviados.";
  - [ ] uma pedindo valor ou prazo inexistente → não inventou;
  - [ ] uma com documentos em conflito → mostrou os dois e escreveu "CONFLITO ENTRE DOCUMENTOS — A CONFIRMAR".
- [ ] Todas as respostas trouxeram documento, versão, data e item.
- [ ] Defini quem atualiza os documentos e quando o teste é repetido.

## Antes de usar uma resposta (30 segundos)

- [ ] Abri o documento citado no item indicado.
- [ ] O trecho entre aspas está lá, com as mesmas palavras.
- [ ] A versão citada é a vigente.
- [ ] A resposta não acrescentou prazo, valor, nome ou condição que não está no trecho.
- [ ] Se havia "A CONFIRMAR" ou "CONFLITO", falei com o dono do documento antes de responder ao cliente ou funcionário.

## Quando trocar um documento

- [ ] Atualizei versão, data e estado no cabeçalho.
- [ ] Removi do assistente a versão antiga.
- [ ] Repeti o roteiro de testes.
