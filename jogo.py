import random; num = random.randint(1, 10); print("Pensei num numero de 1 a 10!"); tentativa = int(input("Tenta adivinhar: ")); 
if tentativa == num: print("ACERTOU! Tu e brabo mesmo!")
else: print(f"Errou! Era {num}. Tenta de novo!")
