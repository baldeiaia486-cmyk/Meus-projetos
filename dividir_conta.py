print("=== Dividir Conta 🍽️ ===")

total = float(input("Quanto foi a conta total? Ex: 15000: "))
pessoas = int(input("Quantas pessoas vão dividir? Ex: 3: "))

gorjeta = input("Vão dar gorjeta de 10%? (sim/não): ").lower()

if gorjeta == "sim":
    total = total + (total * 0.10)
    print(f"Com gorjeta, total ficou: {total:.0f} FCFA")

cada_um = total / pessoas

print(f"\n💰 Total: {total:.0f} FCFA")
print(f"👥 {pessoas} pessoas")
print(f"👉 Cada um paga: {cada_um:.0f} FCFA")

if cada_um > 10000:
    print("Eita, restaurante caro! 😅 Da próxima é no mercado de Bandim!")
elif cada_um > 5000:
    print("Preço justo, dá pra repetir 👍")
else:
    print("Baratinho! Bora repetir amanhã! 🎉")
