print("=== Quiz de Bissau 🇬🇼 ===")
pontos = 0

print("\n1. Qual é a capital da Guiné-Bissau?")
r1 = input("a) Bafatá  b) Bissau  c) Cacheu: ").lower()
if r1 == "bissau" or r1 == "b":
    print("Certo! ✅")
    pontos += 1
else:
    print("Errado, é Bissau!")

print("\n2. Qual é a moeda da Guiné-Bissau?")
r2 = input("a) Naira  b) FCFA  c) Escudo: ").lower()
if r2 == "fcfa" or r2 == "b":
    print("Certo! ✅")
    pontos += 1
else:
    print("Errado, é FCFA!")

print("\n3. Qual língua se fala em Bissau?")
r3 = input("a) Crioulo  b) Francês  c) Inglês: ").lower()
if r3 == "crioulo" or r3 == "a":
    print("Certo! ✅")
    pontos += 1
else:
    print("Errado, é Crioulo!")

print(f"\nTu fizeste {pontos}/3 pontos!")
if pontos == 3:
    print("100% Bissauense! 🎉")
elif pontos == 2:
    print("Quase lá! 💪")
else:
    print("Bora estudar mais Bissau! 📚")
