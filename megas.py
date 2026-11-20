print("=== Contador de Megas 📱 ===")
nome = input("Teu nome: ")

megas_dia = float(input("Quantos megas gastas por dia? Ex: 500: "))
dias = int(input("Quantos dias por mês usas internet? Ex: 30: "))

total_mes = megas_dia * dias
total_gb = total_mes / 1000
custo = total_gb * 3000  # 3000 FCFA por GB mais ou menos

print(f"\n{nome}, tu gastas:")
print(f"📊 {total_mes:.0f} megas por mês")
print(f"📦 Isso é {total_gb:.1f} GB")
print(f"💰 Custa mais ou menos {custo:.0f} FCFA por mês")

if total_gb > 10:
    print("Eita, gastas muito! 😅 Bora poupar megas e usar Wi-Fi?")
elif total_gb > 5:
    print("Tá normal, usas bem a net 👍")
else:
    print("Boa! Tu és poupado, gastas pouco! 🎉")
