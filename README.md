# generator-contract
Generator Contract Prestari Servicii
## In root folder ai nevoie de un fisier contract.dox cu placeholdere de forma {{nume_societate}} 

 Vezi clasa dateBeneficiar din fisierul dateBeneficiar.py pentru celelalte variabile

```python
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
```
