from datetime import datetime
class DateBeneficiar:
    def __init__(self):
        # Obține data de azi în format "dd/mm/yyyy"
        data_curenta = datetime.now()
        self.data = data_curenta.strftime("%d/%m/%Y")
        self.nr_contract = int(input("Introdu numarul contractului: "))
        self.nume_societate = str(input("Numele Societatii: "))
        self.j_societate = str(input("J de forma: J08/2387/2019: "))
        self.CUI_societate = str(input("CUI Societate: "))
        self.nume_reprezentant_legal = str(input("Nume Reprezentant Legal: "))
        self.email_beneficiar = str(input("Adresa Email Beneficiar: "))
        self.numar_telefon_beneficiar = str(input("Numar Telefon Beneficiar: "))
        self.site_beneficiar = str(input("Site Beneficiar: "))
        self.fee = str(input("FEE urmat de valuta de exemplu 100 lei sau 100 EUR: "))
       
        def cere_date(self):
            output = f"Nume Societate: {self.nume_societate}\n"
            output += f"J: {self.j_societate}\n"
            output += f"CUI Societate: {self.CUI_societate}\n"
            output += f"Nume Reprezentant Legal: {self.nume_reprezentant_legal}\n"
            output += f"Adresa Email Beneficiar: {self.email_beneficiar}\n"
            output += f"Numar Telefon Beneficiar: {self.numar_telefon_beneficiar}\n"
            output += f"Site Beneficiar: {self.site_beneficiar}\n"
            output += f"Data: {self.data}\n"
            output += f"Numar Contract: {self.nr_contract}\n"

            return output