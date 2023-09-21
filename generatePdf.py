from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def generate_pdf(input_file, output_file):
    document = Document(input_file)

    # Deschide un fișier PDF pentru scriere
    c = canvas.Canvas(output_file, pagesize=A4)

    # Iterează prin paragrafele din șablonul Word și adaugă textul în PDF
    for paragraph in document.paragraphs:
        for run in paragraph.runs:
            c.drawString(100, 700, run.text)  # Ajustează coordonatele și formatarea aici

    # Salvează paginile PDF și închide fișierul
    c.showPage()
    c.save()