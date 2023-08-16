import cv2
import tkinter as tk
from PIL import Image, ImageTk

def capture_and_show():
    _, frame = camera.read()  # Capturar um frame da câmera
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Converter o formato de cor
    img = Image.fromarray(frame)  # Criar um objeto Image a partir do array
    img_tk = ImageTk.PhotoImage(image=img)  # Converter para formato compatível com tkinter
    label.config(image=img_tk)  # Atualizar o componente Label com a nova imagem
    label.image = img_tk  # Manter uma referência para evitar que a imagem seja coletada pelo garbage collector

    if countdown_started:
        draw_countdown()
    
    root.after(10, capture_and_show)  # Chamar a função novamente após 10ms

def save_image():
    _, frame = camera.read()
    cv2.imwrite("captured_image.jpg", frame)


def draw_countdown():
    global countdown, countdown_label
    
    if countdown > 0:
        countdown_label.config(text=str(countdown))
        countdown -= 1
        root.after(1000, draw_countdown)
    else:
        countdown_label.config(text="")
        countdown_started = False

def start_countdown():
    global countdown, countdown_started
    countdown = 5  # Definir o tempo da contagem regressiva em segundos
    countdown_started = True
    draw_countdown()

# Inicialização do OpenCV
camera = cv2.VideoCapture(0)

# Inicialização do Tkinter
root = tk.Tk()
root.title("Captura e Salvamento de Imagem")
# root.wm_attributes('-transparentcolor', '#ab23ff')

# Criar um componente Label para mostrar a imagem capturada
label = tk.Label(root)
label.pack()


# Criar um botão para salvar a imagem
save_button = tk.Button(root, text="Salvar Imagem", command=save_image)
save_button.pack()

start_button = tk.Button(root, text="Iniciar Contagem Regressiva", command=start_countdown)
start_button.pack()
start_button.place(x=100, y=100)

countdown_label = tk.Label(root, font=("Helvetica", 48), bg='#ab23ff') 
countdown_label.pack()
countdown_label.place(relx=0.5, rely=0.5, anchor="center")

over_label = tk.Label(root, font=("Helvetica", 48), text='Alguma Coisa') 
over_label.pack()
over_label.place(relx=0.5, rely=0.3, anchor="center")

countdown = 0
countdown_started = False

# Chamar a função de captura e exibição
capture_and_show()

# Iniciar o loop principal do Tkinter
root.mainloop()

# Liberar os recursos
camera.release()
cv2.destroyAllWindows()
