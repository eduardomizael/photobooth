from PIL import Image
import datetime
from pathlib import Path
import shutil

class ImageComposer:
    bg = Image.open("elements/background.png").convert("RGBA")
    overlay = Image.open("elements/photo_overlay.png").convert("RGBA")
    media_bg = Image.open("elements/media_bg.png").convert("RGBA")
    media_overlay = Image.open("elements/media_overlay.png").convert("RGBA")
    photo_local_dir = Path('photos')
    media_local_dir = Path('media')
    photo_network_dir = Path(r'\\10.5.0.13\Arquivos\ITU-CCS\photobooth\expo')
    media_network_dir = Path(r'\\10.5.0.13\Arquivos\ITU-CCS\photobooth\social_media')

    def __init__(self, images: list = None) -> None:
        self.images = images

    def photo_compose(self, images: list = None, save: bool = True, copy: bool = True) -> tuple[Image.Image, Path]:
        """Faz a composição das imagens e salva o arquivo em disco.
        :param images: Lista de imagens a serem compostas
        :param save: Se True, salva o arquivo em disco
        :param copy: Se True, copia o arquivo para a rede
        :return: Tupla com a imagem composta e o caminho do arquivo salvo
        """
        images = images or self.images
        if not images:
            raise ValueError("No images to compose")
        
        images = [img.resize((725, 410), Image.LANCZOS) for img in images]
        composed = Image.new("RGBA", self.bg.size)
        composed.paste(self.bg, (0, 0), self.bg)
        composed.paste(images[0], (186, 89), images[0])
        composed.paste(images[1], (1007, 89), images[1])
        composed.paste(images[2], (345, 586), images[2])
        composed.paste(self.overlay, (0, 0), self.overlay)
        
        saved = None
        if save:
            saved = self.save_file(composed, path=self.photo_local_dir)
            if copy:
                self.copy_to_network_dir(saved, self.photo_network_dir)
        return composed, saved
    
    def media_compose(self, images: list = None, save: bool = True, copy: bool = True) -> tuple[Image.Image, Path]:
        """Faz a composição das imagens e salva o arquivo em disco.
        :param images: Lista de imagens a serem compostas
        :param save: Se True, salva o arquivo em disco
        :param copy: Se True, copia o arquivo para a rede
        :return: Tupla com a imagem composta e o caminho do arquivo salvo
        """
        images = images or self.images
        if not images:
            raise ValueError("No images to compose")
        
        images = [img.resize((518, 294), Image.LANCZOS) for img in images]
        composed = Image.new("RGBA", self.media_bg.size)
        composed.paste(self.media_bg, (0, 0), self.media_bg)
        composed.paste(images[0], (82, 43), images[0])
        composed.paste(images[1], (504, 391), images[1])
        composed.paste(images[2], (82, 744), images[2])
        composed.paste(self.media_overlay, (0, 0), self.media_overlay)
        
        saved = None
        if save:
            saved = self.save_file(composed, path=self.media_local_dir)
            if copy:
                self.copy_to_network_dir(saved, self.media_network_dir)
        return composed, saved
    
    def compose_all(self, images: list) -> tuple:
        photo = self.photo_compose(images)
        media = self.media_compose(images)
        return photo, media
    
    def save_file(self, image, path=None, name=None, format="PNG") -> Path:
        """Salva o arquivo em disco.
        :param image: Imagem a ser salva
        :param path: Caminho do arquivo
        :param name: Nome do arquivo
        :param format: Formato do arquivo
        :return: Caminho do arquivo salvo
        """
        path = path or self.photo_local_dir
        if not name:
            name = f"photo_{datetime.datetime.now():%Y%m%d%H%M%S}"
        format = format.lower()
        path.absolute().mkdir(parents=True, exist_ok=True)
        path = path / f"{name}.{format}"
        image.save(path)
        return path

    def copy_to_network_dir(self, src: Path, dst=None) -> Path:
        """Copia o arquivo para o diretório da rede.
        :param src: Caminho do arquivo
        :param dst: Caminho de destino
        :return: Caminho do arquivo copiado
        """
        dst = dst or self.photo_network_dir
        dst = dst / src.name
        # src.replace(dst)
        try:
            shutil.copy2(src, dst)
        except Exception as e:
            print('Erro ao copiar o arquivo para a rede.', e)
        return dst

    def crop_center(self, image, prop='16/9'):
        w_prop, h_prop = [int(p) for p in prop.split('/')]
        w, h = image.size
        if w/h > w_prop/h_prop:
            offset = int(abs(w - h * w_prop / h_prop) / 2)
            crop_settings = (offset, 0, w - offset, h)
        else:
            offset = int(abs(h - w * h_prop / w_prop) / 2)
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


if __name__ == '__main__':
    pass
    # src = Path(r'photos\photo_20230830134234.png').absolute()
    # dst = Path(r'\\10.5.0.13\Arquivos\ITU-CCS\photobooth\expo')
    # ic = ImageComposer()

    # ic.copy_to_network_dir(src, dst)

# Carregar a imagem de fundo e a imagem para sobrepor
    # base = Image.open("fundo01.png").convert("RGBA")
    # overlay = Image.open("overlay01.png").convert("RGBA")

    # image_paths = ['img/img4.webp', 'img/img2.jpg', 'img/img3.jpg']
    # imgs = [Image.open(i).convert('RGBA') for i in image_paths]

    # for i, img in enumerate(imgs):
    #     cropped_img = crop_center(img)
    #     save(cropped_img, name=f'img_{i}_cropped', format='PNG')
