import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Captura e Salvamento de Imagem")
        self.geometry("1920x1080")
        self.resizable(False, False)
        self.attributes("-fullscreen", True)
        self._create_widgets()


    def _create_widgets(self):
        # inserir imagem de fundo na janela
        self.background_image = tk.PhotoImage(file="fundo01.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # colocar a label no nivel mais baixo
        self.background_label.lower()

        # inserir uma label para mostrar a imagem capturada no centro da janela com tamenho de 533x300
        self.label = tk.Label(self, width=533, height=300)
        self.label.place(x=200, y=200, anchor="center")

        # botão de fechar no canto inferior direito
        self.close_button = tk.Button(self, text="Fechar", command=self.destroy)
        # self.close_button.pack()
        self.close_button.place(relx=0.9, rely=0.9, anchor="center")



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()