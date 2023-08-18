from PIL import Image
import datetime

# Carregar a imagem de fundo e a imagem para sobrepor
fundo = Image.open("fundo01.png").convert("RGBA")
img1 = Image.open("img1.jpg").convert("RGBA")
img2 = Image.open("img2.jpg").convert("RGBA")
img3 = Image.open("img3.jpg").convert("RGBA")
overlay = Image.open("overlay01.png").convert("RGBA")

def crop_center(image):
    w, h = image.size
    if w / h > 16 / 9:
        new_h = h
        new_w = h * 16 / 9
        x = (w - new_w) / 2
        y = 0
    else:
        new_w = w
        new_h = w * 9 / 16
        x = 0
        y = (h - new_h) / 2
    return image.crop((x, y, x + new_w, y + new_h))


# redimensionar as imagens para o tamanho de 533x300
img1 = img1.resize((533, 300))
img2 = img2.resize((533, 300))
img3 = img3.resize((533, 300))

# Criar uma nova imagem com o mesmo tamanho da imagem de fundo
nova_imagem = Image.new("RGBA", fundo.size)
nova_imagem.paste(fundo, (0, 0))  # Colar a imagem de fundo na nova imagem
# inserir imagem 1 na posição (250, 118)	
nova_imagem.paste(img1, (250, 118), img1)
# inserir imagem 2 na posição (1119, 118)
nova_imagem.paste(img2, (1119, 118), img2)
# inserir imagem 3 na posição (685, 566)
nova_imagem.paste(img3, (685, 566), img3)
# inserir overlay na posição (0, 0)
# nova_imagem.paste(overlay, (0, 0), overlay)
# abrir a imagem com o visualizador padrão do sistema
# nova_imagem.show()

# Salvar a nova imagem
image_name = f"photo_{datetime.datetime.now():%Y%m%d%H%M%S}.png"
nova_imagem.save(image_name)
