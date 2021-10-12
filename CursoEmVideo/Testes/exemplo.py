import qrcode
imagem = qrcode.make("https://www.youtube.com/cursoemvideo")
imagem.save("qr.jpg")