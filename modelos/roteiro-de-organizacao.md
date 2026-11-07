# Roteiro para organizar os documentos antes de subir

Faça uma vez. Leva o tempo de separar e conferir seus arquivos; a IA não faz esta parte por você.

## 1. Escolha o assunto

Comece por um assunto só (ex.: atendimento, ou regras internas de pessoal). Um assunto bem coberto funciona melhor que tudo misturado.

## 2. Separe os documentos

- Use só documentos **aprovados**. Rascunho fica fora ou com Estado "Rascunho, não usar".
- Uma versão vigente por documento. Versões antigas: tire da pasta ou marque "SUBSTITUÍDA".
- Prefira .docx, .pdf com texto selecionável, .txt ou .md. PDF escaneado como imagem ou protegido contra cópia pode não ser lido (o Gemini Notebook informa que PDF protegido contra cópia falha na importação).

## 3. Tire dados pessoais

Antes de subir, remova CPF, telefone, endereço, salário individual, dados de saúde e qualquer dado de cliente ou funcionário que a consulta não precise. Documento de regra geral não precisa de dado pessoal. Em caso de dúvida sobre a LGPD, consulte quem cuida disso na sua empresa (jurídico ou encarregado de dados). Este material não é parecer jurídico.

## 4. Coloque o cabeçalho

Copie `ficha-de-documento.md` no topo de cada documento: código, versão, data, dono, estado. Numere as seções e itens (1.1, 1.2…). Sem numeração, a IA cita "o documento inteiro" e você perde tempo conferindo.

## 5. Preencha o índice

Liste os documentos em `indice-de-documentos.csv`. Ele serve para você saber o que está no assistente e quando revisar.

## 6. Teste antes de liberar para a equipe

Copie `roteiro-de-testes-modelo.csv`, escreva 8 a 12 perguntas reais da sua equipe e inclua pelo menos:

- 1 pergunta cuja resposta **não** está nos documentos (o certo é "não encontrei");
- 1 pergunta que pede um valor ou prazo que não existe ("me dá um valor aproximado");
- 1 pergunta sobre um assunto em que dois documentos podem discordar.

Só libere quando todas passarem. Repita o teste sempre que trocar um documento.
