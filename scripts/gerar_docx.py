"""Converte arquivos .md simples (títulos, parágrafos, listas, citações e tabelas)
em .docx editáveis, para enviar a um Projeto de IA ou ao Gemini Notebook como
documento do Word.

Uso:
    python gerar_docx.py ENTRADA [ENTRADA ...] --saida PASTA

ENTRADA pode ser um arquivo .md ou uma pasta (converte todos os .md dela).
Não altera os arquivos de entrada. Requer python-docx (ver requirements.txt).
"""

import argparse
import re
import sys
from pathlib import Path

from docx import Document
from docx.shared import Pt

SEPARADOR_TABELA = re.compile(r"^\|?\s*:?-{3,}")


def celulas(linha: str) -> list[str]:
    return [c.strip() for c in linha.strip().strip("|").split("|")]


def texto_simples(texto: str) -> str:
    """Remove marcações de negrito e código; mantém o texto."""
    texto = re.sub(r"\*\*(.+?)\*\*", r"\1", texto)
    texto = re.sub(r"`(.+?)`", r"\1", texto)
    return texto


def converter(origem: Path, destino: Path) -> int:
    linhas = origem.read_text(encoding="utf-8").splitlines()
    doc = Document()
    estilo = doc.styles["Normal"]
    estilo.font.name = "Calibri"
    estilo.font.size = Pt(11)

    blocos = 0
    i = 0
    while i < len(linhas):
        linha = linhas[i].rstrip()
        if not linha.strip():
            i += 1
            continue
        if linha.startswith("|"):
            grupo = []
            while i < len(linhas) and linhas[i].strip().startswith("|"):
                if not SEPARADOR_TABELA.match(linhas[i].strip().strip("|").strip()):
                    grupo.append(celulas(linhas[i]))
                i += 1
            colunas = max(len(g) for g in grupo)
            tabela = doc.add_table(rows=len(grupo), cols=colunas)
            tabela.style = "Table Grid"
            for r, linha_tab in enumerate(grupo):
                for c in range(colunas):
                    valor = linha_tab[c] if c < len(linha_tab) else ""
                    tabela.cell(r, c).text = texto_simples(valor)
                    if r == 0:
                        for run in tabela.cell(r, c).paragraphs[0].runs:
                            run.bold = True
            doc.add_paragraph()
            blocos += 1
            continue
        titulo = re.match(r"^(#{1,4})\s+(.*)$", linha)
        if titulo:
            doc.add_heading(texto_simples(titulo.group(2)), level=len(titulo.group(1)))
        elif linha.startswith(">"):
            p = doc.add_paragraph(texto_simples(linha.lstrip("> ").strip()))
            for run in p.runs:
                run.italic = True
        elif re.match(r"^\s*[-*]\s+", linha):
            doc.add_paragraph(texto_simples(re.sub(r"^\s*[-*]\s+", "", linha)), style="List Bullet")
        else:
            doc.add_paragraph(texto_simples(linha))
        blocos += 1
        i += 1

    destino.parent.mkdir(parents=True, exist_ok=True)
    doc.save(destino)
    return blocos


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("entradas", nargs="+", help="arquivos .md ou pastas")
    parser.add_argument("--saida", required=True, help="pasta onde salvar os .docx")
    args = parser.parse_args()

    arquivos: list[Path] = []
    for entrada in args.entradas:
        p = Path(entrada)
        if p.is_dir():
            arquivos.extend(sorted(p.glob("*.md")))
        elif p.suffix.lower() == ".md" and p.exists():
            arquivos.append(p)
        else:
            print(f"Ignorado (não é .md nem pasta): {p}", file=sys.stderr)

    if not arquivos:
        print("Nenhum .md encontrado.", file=sys.stderr)
        return 1

    saida = Path(args.saida)
    for arquivo in arquivos:
        destino = saida / (arquivo.stem + ".docx")
        blocos = converter(arquivo, destino)
        print(f"{arquivo.name} -> {destino} ({blocos} blocos)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
