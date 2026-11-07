# Script opcional: converter .md em .docx

Você **não precisa** deste script para usar a solução. Os documentos de exemplo já estão prontos em .md e em .docx (`exemplos/entrada-ficticia/docx/`).

Ele serve para quem escreve os documentos em Markdown (.md) e quer enviá-los como Word.

## Como rodar (Windows, Mac ou Linux)

1. Tenha Python 3 instalado (testado com 3.11.9).
2. Na pasta do repositório, crie um ambiente isolado e instale a dependência:

```bash
python -m venv .venv
# Windows:  .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate
pip install -r scripts/requirements.txt
```

3. Converta uma pasta ou arquivos:

```bash
python scripts/gerar_docx.py exemplos/entrada-ficticia --saida exemplos/entrada-ficticia/docx
```

O script lê títulos (#), parágrafos, listas (-), citações (>) e tabelas (|). Não altera os .md originais. Formatação mais complexa (imagens, links, negrito no meio da frase) vira texto simples.

Testado em 02/11/2026 com os documentos fictícios; registro em `exemplos/entrada-ficticia/docx/execucao-2026-11-02.txt`.
