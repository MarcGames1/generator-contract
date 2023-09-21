from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from inlocuiesteDatele import inlocuieste_date_cu_date_beneficiar
from generatePdf import generate_pdf
from dateBeneficiar import DateBeneficiar

        


def main():
    
    # Deschide șablonul Word
    sablon_file = "./contract.docx"
    document = Document(sablon_file)
    # Date Contract
    date_beneficiar = DateBeneficiar()
    # Output Fisier
    output_file_docx = f"{date_beneficiar.nume_societate}.docx"
    
    inlocuieste_date_cu_date_beneficiar(document, date_beneficiar)
    document.save(output_file_docx)
    


if __name__ == "__main__":
    main()