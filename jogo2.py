import random
num = random.randint(1, 10)
print("Pensei num numero de 1 a 10!")
while True:
    t = int(input("Chute: "))
    if t == num:
        print("BOOOA IANIS! ACERTOU! TU É BRABO!")
        break
    elif t < num:
        print("Maior! Tenta um numero maior")
    else:
        print("Menor! Tenta um menor")
