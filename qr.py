import qrcode

texto = input("O que vai no QR Code? (link ou texto): ")

# Cria o QR Code
img = qrcode.make(texto)
img.save("meu_qr.png")

print("✅ QR Code criado! Arquivo: meu_qr.png")
print("Tá na pasta do Termux, abre na galeria!")
