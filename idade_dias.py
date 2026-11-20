print("=== Quantos dias tu já viveste? ===")
idade = int(input("Quantos anos tens? Ex: 17: "))

dias = idade * 365
horas = dias * 24
minutos = horas * 60

print(f"\nTu tens {idade} anos, isso é:")
print(f"📅 {dias} dias")
print(f"⏰ {horas} horas")
print(f"⏱️ {minutos} minutos")

if idade < 18:
    print("Ainda és jovem, bora aproveitar! 🚀")
else:
    print("Já és adulto, bora codar forte! 💪")
