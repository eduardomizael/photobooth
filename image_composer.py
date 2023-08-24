from PIL import Image
import datetime

def crop_center(image):
    w, h = image.size
    if w/h > 16/9:
        offset = int(abs(w - h * 16 / 9) / 2)
        crop_settings = (offset, 0, w - offset, h)
    else:
        offset = int(abs(h - w * 9 / 16) / 2)
        crop_settings = (0, offset, w, h - offset)
    
    return image.crop(crop_settings)


def resize(image, size=(533, 300)):
    return image.resize(size)


def compose(base, overlay, images):
    composed = Image.new("RGBA", base.size)
    composed.paste(images[0], (250, 118), images[0])
    composed.paste(images[1], (1119, 118), images[1])
    composed.paste(images[2], (685, 566), images[2])
    composed.paste(overlay, (0, 0), overlay)
    return composed


def save(image, name=None, format="PNG"):
    if not name:
        name = f"photo_{datetime.datetime.now():%Y%m%d%H%M%S}"
    format = format.lower()
    image.save(f'{name}.{format}', format)


if __name__ == '__main__':
    
# Carregar a imagem de fundo e a imagem para sobrepor
    base = Image.open("fundo01.png").convert("RGBA")
    overlay = Image.open("overlay01.png").convert("RGBA")

    image_paths = ['img/img4.webp', 'img/img2.jpg', 'img/img3.jpg']
    imgs = [Image.open(i).convert('RGBA') for i in image_paths]

    for i, img in enumerate(imgs):
        cropped_img = crop_center(img)
        save(cropped_img, name=f'img_{i}_cropped', format='PNG')
