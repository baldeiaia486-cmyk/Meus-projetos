import random
num = random.randint(1, 20)
print("Adivinha 1 a 20!")
while True:
    chute = int(input("Chute: "))
    if chute == num:
        print("Acertou! 🎉")
        break
    elif chute < num:
        print("Maior...")
    else:
        print("Menor...")

