"""Genera el PDF de cada capítulo a partir de sus apartados en Markdown.

Uso: python herramientas/generar_pdf.py [01-seguridad ...]
Sin argumentos genera todos los capítulos.
"""

import os
import subprocess
import sys
from pathlib import Path

import markdown

RAIZ = Path(__file__).resolve().parents[1]
CARPETA_CAPITULOS = RAIZ / "capitulos"
CARPETA_PDF = RAIZ / "pdf"
CARPETA_TEMPORAL = RAIZ / "build"
HOJA_DE_ESTILO = Path(__file__).with_name("estilo_libro.css")
PREFIJO_PDF = "libro-web-2026-"
EXTENSIONES_MARKDOWN = ["tables", "fenced_code", "sane_lists"]
NAVEGADOR_POR_DEFECTO = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# Chrome sin ventana imprime la página igual que la vería un lector, tablas incluidas.
OPCIONES_NAVEGADOR = ["--headless=new", "--disable-gpu", "--no-pdf-header-footer"]
PLANTILLA_HTML = """<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><title>{titulo}</title>
<style>{estilo}</style></head><body>{cuerpo}</body></html>"""


def leer_capitulo(carpeta: Path) -> str:
    apartados = sorted(carpeta.glob("*.md"))
    return "\n\n".join(apartado.read_text(encoding="utf-8") for apartado in apartados)


def escribir_html(carpeta: Path) -> Path:
    cuerpo = markdown.markdown(leer_capitulo(carpeta), extensions=EXTENSIONES_MARKDOWN)
    estilo = HOJA_DE_ESTILO.read_text(encoding="utf-8")
    titulo = f"{PREFIJO_PDF}{carpeta.name}"
    CARPETA_TEMPORAL.mkdir(exist_ok=True)
    destino = CARPETA_TEMPORAL / f"{titulo}.html"
    destino.write_text(PLANTILLA_HTML.format(titulo=titulo, estilo=estilo, cuerpo=cuerpo), encoding="utf-8")
    return destino


def imprimir_pdf(html: Path) -> Path:
    navegador = os.environ.get("NAVEGADOR_PDF", NAVEGADOR_POR_DEFECTO)
    perfil = CARPETA_TEMPORAL / "perfil-navegador"
    CARPETA_PDF.mkdir(exist_ok=True)
    destino = CARPETA_PDF / f"{html.stem}.pdf"
    orden = [navegador, *OPCIONES_NAVEGADOR, f"--user-data-dir={perfil}", f"--print-to-pdf={destino}", html.as_uri()]
    subprocess.run(orden, check=True, capture_output=True)
    return destino


def generar_capitulo(carpeta: Path) -> None:
    pdf = imprimir_pdf(escribir_html(carpeta))
    print(f"PDF generado: {pdf.relative_to(RAIZ)}")


def elegir_capitulos(nombres: list[str]) -> list[Path]:
    todos = sorted(ruta for ruta in CARPETA_CAPITULOS.iterdir() if ruta.is_dir())
    if not nombres:
        return todos
    return [ruta for ruta in todos if ruta.name in nombres]


if __name__ == "__main__":
    for capitulo in elegir_capitulos(sys.argv[1:]):
        generar_capitulo(capitulo)
