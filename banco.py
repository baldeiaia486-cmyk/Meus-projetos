print("=== Banco de Bissau 🏦 ===")
nome = input("Teu nome: ")
saldo = 10000
print(f"\nOlá {nome}! Teu saldo inicial é {saldo} FCFA")

# Depositar
deposito = float(input("\nQuanto queres depositar? "))
saldo = saldo + deposito
print(f"Depositaste {deposito:.0f} FCFA. Saldo agora: {saldo:.0f} FCFA")

# Levantar
levantar = float(input("\nQuanto queres levantar? "))
if levantar <= saldo:
    saldo = saldo - levantar
    print(f"Levantaste {levantar:.0f} FCFA ✅")
else:
    print("Saldo insuficiente! 😅")

print(f"\n💰 Teu saldo final é: {saldo:.0f} FCFA")

if saldo >= 50000:
    print("Estás rico! 🎉")
elif saldo >= 20000:
    print("Boa, estás a juntar bem! 💪")
else:
    print("Bora juntar mais amanhã! 🚀")
