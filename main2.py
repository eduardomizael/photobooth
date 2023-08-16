import cv2
import time

def draw_countdown(frame, countdown):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 3
    font_thickness = 5
    text_size = cv2.getTextSize(str(countdown), font, font_scale, font_thickness)[0]
    text_x = (frame.shape[1] - text_size[0]) // 2
    text_y = (frame.shape[0] + text_size[1]) // 2
    cv2.putText(frame, str(countdown), (text_x, text_y), font, font_scale, (0, 0, 255), font_thickness, cv2.LINE_AA)

def capture_photos(interval, num_photos):
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Não foi possível abrir a câmera.")
        return

    # Configurações para salvar o vídeo temporário
    frame_width = int(camera.get(3))
    frame_height = int(camera.get(4))
    video_temp = cv2.VideoWriter('video_temp.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (frame_width, frame_height))

    for i in range(num_photos):
        ret, frame = camera.read()

        if not ret:
            print("Não foi possível capturar a imagem.")
            break

        # Cria um vídeo temporário mostrando o fluxo contínuo
        video_temp.write(frame)

        # Contagem regressiva antes de tirar a foto
        for countdown in range(3, 0, -1):
            draw_countdown(frame, countdown)
            cv2.imshow("Photobooth", frame)
            cv2.waitKey(1000)

        # Salva a foto atual
        timestamp = time.time()
        image_name = f"photo_{i+1}_{timestamp}.png"
        cv2.imwrite(image_name, frame)

    # Libera recursos
    video_temp.release()
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    intervalo_entre_fotos = 5  # Intervalo em segundos entre cada foto
    numero_de_fotos = 5        # Número total de fotos a serem tiradas

    capture_photos(intervalo_entre_fotos, numero_de_fotos)
