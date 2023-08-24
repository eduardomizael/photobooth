import cv2
import tkinter as tk
from PIL import Image, ImageTk

class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela de Captura")
        self.root.attributes("-fullscreen", True)  # Definir para modo fullscreen

        # Inicialização do OpenCV
        self.camera = cv2.VideoCapture(0)

        # Carregar a imagem de fundo e redimensioná-la para o tamanho da janela
        self.background_image = Image.open("fundo01.png")
        self.background_image = self.background_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Criar um componente Label para mostrar a imagem de fundo
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Criar um componente Label para mostrar a imagem capturada
        self.cam_frame = tk.Canvas(self.root, bg='black', width=1024, height=768, border=0)
        self.cam_frame.place(relx=0.5, rely=0.5, anchor="center")
        # self.label = tk.Label(self.root)
        # self.label.place(relx=0.5, rely=0.5, anchor="center")
        
        # self.overlay_image = Image.open("img/3b.png").convert("RGBA").resize((1024, 768))
        # self.overlay_image = ImageTk.PhotoImage(self.overlay_image)
        outra_imagem = ImageTk.PhotoImage(file="fundo01.png")
        # self.cam_frame.create_image(100, 200, image=outra_imagem)
        # w, h = self.overlay_image.width(), self.overlay_image.height()
        # self.overlay_canvas = tk.Canvas(self.root, bg='black', width=w, height=h)
        # self.overlay_canvas.place(relx=0.5, rely=0.5, anchor="center")
        # self.cam_frame.create_image(0, 0, image=outra_imagem)
        # self.cam_frame.create_image(w/2, h/2, image=self.overlay_image)
        # self.overlay_label = tk.Label(self.root, bg='blue', image=self.overlay_image)
        # self.overlay_label.place(relx=0.5, rely=0.5, anchor="center")

        self.close_button = tk.Button(self.root, text="Fechar", command=self.root.destroy)
        self.close_button.place(relx=0.9, rely=0.9, anchor="center")
        # self.close_button.pack()

        self.show_frame_button = tk.Button(self.root, text="Mostrar Frame Capturado", command=self.show_current_frame)
        self.show_frame_button.place(relx=0.9, rely=0.8, anchor="center")

        self.capture_and_show()

    def capture_and_show(self):
        _, frame = self.camera.read()  # Capturar um frame da câmera
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Converter o formato de cor
        img = Image.fromarray(frame)  # Criar um objeto Image a partir do array
        img_tk = ImageTk.PhotoImage(image=img)  # Converter para formato compatível com tkinter
        # self.label.config(image=img_tk)  # Atualizar o componente Label com a nova imagem
        # self.label.image = img_tk  # Manter uma referência para evitar que a imagem seja coletada pelo garbage collector
        self.cam_frame.create_image(0, 0, image=img_tk)
        self.root.after(10, self.capture_and_show)  # Chamar a função novamente após 10ms

    def show_current_frame(self):
        _, frame = self.camera.read()  # Capturar um frame da câmera
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Converter o formato de cor
        img = Image.fromarray(frame)  # Criar um objeto Image a partir do array

        # Criar uma nova janela para mostrar o frame capturado
        frame_window = tk.Toplevel(self.root)
        frame_window.title("Frame Capturado")

        # Converter a imagem para formato compatível com tkinter
        img_tk = ImageTk.PhotoImage(image=img)
        label = tk.Label(frame_window, image=img_tk)
        label.image = img_tk
        label.pack()

    def run(self):
        self.root.mainloop()

        # Liberar os recursos
        self.camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
    app.run()
