import random, string
senha = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
print(f"Sua senha: {senha}")
