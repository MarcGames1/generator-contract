

def inlocuieste_date_cu_date_beneficiar(document, date_beneficiar):
    plachete = {
        "{{nr_contract}}": date_beneficiar.nr_contract,
        "{{nume_societate}}": date_beneficiar.nume_societate,
        "{{data}}": date_beneficiar.data,
        "{{j_societate}}": date_beneficiar.j_societate,
        "{{CUI_Societate}}": date_beneficiar.CUI_societate,
        "{{nume_reprezentant_legal}}": date_beneficiar.nume_reprezentant_legal,
        "{{email_beneficiar}}": date_beneficiar.email_beneficiar,
        "{{numar_telefon_beneficiar}}": date_beneficiar.numar_telefon_beneficiar,
        "{{site_beneficiar}}": date_beneficiar.site_beneficiar,
        "{{fee}}": date_beneficiar.fee
    }

    def exista_placeholder(plachete, text):
        """
        Verifică dacă există cel puțin un placeholder în text.

        :param plachete: Dicționarul cu plachete (chei)
        :param text: Textul în care se efectuează verificarea
        :return: True dacă cel puțin un placeholder există în text, False în caz contrar
        """
        for placeholder in plachete.keys():
            if placeholder in text:
             return True
        return False    



    while True:  # Bucla va rula cel puțin o dată
        text= " "
        for paragraph in document.paragraphs:
            for run in paragraph.runs:
               for placeholder, valoare in plachete.items():
                   run.text = run.text.replace(placeholder, str(valoare))
                   text= run.text
        for table in document.tables:
           for row in table.rows:
               for cell in row.cells:
                   for placeholder, valoare in plachete.items():
                       cell.text = cell.text.replace(placeholder, str(valoare))
                       text= cell.text
        
        if not exista_placeholder(plachete, text):
            break  # Ieșiți din buclă dacă nu mai există placeholdere