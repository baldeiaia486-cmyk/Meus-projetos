from datetime import date

dia = int(input("Dia que nasceste: "))
mes = int(input("Mês (1-12): "))

hoje = date.today()
ano = hoje.year
aniv = date(ano, mes, dia)

if aniv < hoje:
    aniv = date(ano+1, mes, dia)

faltam = (aniv - hoje).days
print(f"\nFaltam {faltam} dias pro teu aniversário! 🎂")
if faltam == 0:
    print("PARABÉNS!!! Hoje é teu dia!")
