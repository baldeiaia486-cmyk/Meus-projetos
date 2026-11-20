print("=== Calculadora de Troco 🧮 ===")

preco = float(input("Quanto custou a compra? Ex: 3500: "))
pago = float(input("Quanto deste? Ex: 5000: "))

troco = pago - preco

print(f"\nCompra: {preco:.0f} FCFA")
print(f"Pagaste: {pago:.0f} FCFA")

if troco < 0:
    print(f"Falta {abs(troco):.0f} FCFA! 😅 Bora completar?")
elif troco == 0:
    print("Troco zero! Pagaste certinho! ✅")
else:
    print(f"Teu troco é: {troco:.0f} FCFA 💰")
    print("Confere antes de sair do mercado!")

    # Conta as notas
    if troco >= 1000:
        print("Deve ter nota de 1000 aí! 👀")
    elif troco >= 500:
        print("Deve ter moeda de 500! 🪙")
