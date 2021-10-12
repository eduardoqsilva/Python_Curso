import qrcode
conteudo = str(input("Digite o conteudo que o qr code deve mostrar: "))
imagem = qrcode.make(f"{conteudo}")
imagem.save("C:/Users/Eduar/OneDrive/Área de Trabalho/qr.jpg")