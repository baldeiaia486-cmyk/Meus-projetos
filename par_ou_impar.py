import random

print("=== Jogo Par ou Ímpar ===")
print("Tu escolhes Par ou Ímpar, depois jogas um número de 0 a 10")

escolha = input("Escolhes par ou impar? ").lower()

tu = int(input("Teu número (0 a 10): "))
pc = random.randint(0, 10)

soma = tu + pc
resultado = "par" if soma % 2 == 0 else "impar"

print(f"\nTu jogaste {tu}, PC jogou {pc}")
print(f"Soma = {soma} -> é {resultado}!")

if escolha == resultado:
    print("Tu ganhaste! 🎉")
else:
    print("PC ganhou! 😅 Tenta de novo")
