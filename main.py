import cv2
import time
from threading import Timer
from datetime import datetime

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

    for i in range(num_photos):
        ret, frame = camera.read()

        if not ret:
            print("Não foi possível capturar a imagem.")
            break

        # Contagem regressiva antes de tirar a foto
        for countdown in range(3, 0, -1):
            draw_countdown(frame, countdown)
            cv2.imshow("Photobooth", frame)
            cv2.waitKey(1000)

        timestamp = time.time()
        image_name = f"photo_{i+1}_{timestamp}.png"

        cv2.imshow("Photobooth", frame)

        # Aguarde o intervalo em segundos antes de capturar a próxima foto
        time.sleep(interval)

        # Salve a imagem capturada
        cv2.imwrite(image_name, frame)

        # Encerre a captura quando a tecla 'q' for pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


def take_picture(frame):
    print("Take picture")
    timestamp = time.time()
    image_name = f"photo_{timestamp}.png"
    cv2.imwrite(image_name, frame)


if __name__ == "__main__":
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Não foi possível abrir a câmera.")
        exit()
    interval = 5
    num_photos = 5

    # x1, y1 = 160, 40
    # x2, y2 = 960, 640

    start_time = time.time()
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Não foi possível capturar a imagem.")
            break
        
        time_passed = time.time() - start_time
        if (time_passed - interval) < 3:
            countdown = 3 - int(time_passed)
            draw_countdown(frame, countdown)
            cv2.imshow("Photobooth", frame)
        else:
            cv2.imshow("Photobooth", frame)

        time_passed = time.time() - start_time
        if time_passed > interval:
            take_picture(frame)
            start_time = time.time()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    

    #     # Encerre a captura quando a tecla 'q' for pressionada
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         camera.release()
    #         cv2.destroyAllWindows()
    #         break
    # intervalo_entre_fotos = 5  # Intervalo em segundos entre cada foto
    # numero_de_fotos = 5        # Número total de fotos a serem tiradas

    # capture_photos(intervalo_entre_fotos, numero_de_fotos)
