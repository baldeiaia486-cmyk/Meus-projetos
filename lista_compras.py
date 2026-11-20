print("=== Lista de Compras - Mercado de Bissau 🛒 ===")

total = 0
itens = []

while True:
    produto = input("\nProduto (ou escreve 'fim' para terminar): ")
    if produto.lower() == "fim":
        break

    preco = float(input(f"Preço de {produto} em FCFA: "))
    total += preco
    itens.append(f"{produto} - {preco:.0f} FCFA")
    print(f"Adicionado! Total até agora: {total:.0f} FCFA")

print("\n--- Tua Lista Final ---")
for item in itens:
    print(f"✅ {item}")

print(f"\n💰 TOTAL: {total:.0f} FCFA")
print(f"📦 Total de itens: {len(itens)}")

if total > 20000:
    print("Eita, ficou caro! 😅 Bora tirar algo?")
elif total > 10000:
    print("Tá no preço normal de Bissau 👍")
else:
    print("Boa! Compra leve e barata! 🎉")

