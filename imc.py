nome = input("Teu nome: ")
peso = float(input("Peso kg: "))
altura = float(input("Altura m: "))

# Se digitar 175, converte pra 1.75 automaticamente
if altura > 3:
    altura = altura / 100

imc = peso / (altura*altura)
print(f"\n{nome}, IMC: {imc:.1f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal ✅")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")
