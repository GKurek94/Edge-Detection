import cv2
from datetime import datetime

# Przechwycenie obraz u kamery, dla wartości 0 jest to kamera wbudowana w laptopa, dla wartości 1 jest to kamera przy mikroskopie
camera = cv2.VideoCapture(0)

# licznik przechwyconych obrazów
photo_counter = 0
# pomoc dla operatora, w celu zrobienia zdjęcia obrazu należy nacisnąc przycisk "S", w celu zamknięcia programu "Q"
print('Press:\n[S] to capture photos\n[Q] to exit')
#pętla umożliwijąca ciągła pracę programu do momentu jej przerwania
while True:
    return_value, image = camera.read()
    image = cv2.imread('test4.jpg')
    #przetworzenie na przestrzeń kolorów BGRA, rozwiniętą o parametr alpha definijący przeźroczystość
    image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    # zastosowanie filtracji gaussowskiej
    image_blurred = cv2.GaussianBlur(image, (5, 5), 0)
    #przetworzenie obrazu na odcień szary
    gray = cv2.cvtColor(image_blurred, cv2.COLOR_BGR2GRAY)
    # zastosowanie metody detekcji krawędzi Sobel
    grad_x = cv2.Sobel(gray, cv2.CV_16S, 1, 0, ksize=3)  # Horyzostalny detektor
    grad_y = cv2.Sobel(gray, cv2.CV_16S, 0, 1, ksize=3)  # Wertykalny detektor
    #zastosowanie metody detekcji krawędzi Canny
    canny = cv2.Canny(image, 100,100)
    #przedstawienie wyników metody Canny w oknie o nazwie Canny
    cv2.imshow("Canny",canny)
    edges = cv2.GaussianBlur(canny, (5, 5), 0)
    #zastosowanie metody progowania Otsu dla wyników
    ret3, th3 = cv2.threshold(edges, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    edges = cv2.cvtColor(th3, cv2.COLOR_BGR2BGRA)
    #połączenie horyzostalnej i wertykalnej dekecji krawędzi Sobel w jeden obraz
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    grad = cv2.cvtColor(grad, cv2.COLOR_BGR2BGRA)

    # stworzenie jednego okna przedstawiającego wyniki w czasie rzeczywistym
    img_concatenated = cv2.hconcat([image, edges])
    cv2.imshow('image', img_concatenated)
    ret, thresh1 = cv2.threshold(grad, 50, 255, cv2.THRESH_BINARY)
    #prowadzenie opóźnienia 50ms po przyciśnieciu klawiszy
    key_pressed = cv2.waitKey(delay=50)
    # funkcja jeżeli dotycząca reakcji programu na wciśniecie przycisków S i Q
    if key_pressed & 0xFF == ord('s'):
        photo_counter += 1
        photo_capture_time = datetime.now().strftime('%d.%m.%Y-%H.%M.%S')
        photo_name = f'{photo_counter}-zdjecie-{photo_capture_time}.jpg'
        edge_name = f'{photo_counter}-krawedz-{photo_capture_time}.jpg'
        cv2.imwrite(photo_name, image)
        cv2.imwrite(edge_name, edges)
        print(photo_capture_time, ': ', photo_counter, '. photo captured.', sep='')
    elif key_pressed & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()