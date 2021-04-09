import numpy as np
import cv2 as cv
#definicja pomocniczych parametrów
def valueLow(x):
    pass
def valueHigh(x):
    pass
#stworzenie okna dla paska śledzenia oraz nazwanie go "Tracking Bar"
img=np.zeros((1000,700,3),np.uint8)
cv.namedWindow("TrackingImage")
#odbiór obrazu z kamery (dla kamery przy mikroskopie trzeba zmienić parametr na 1
camera = cv.VideoCapture(0)
#stworzenie pasków śledzenia dla parametrów detekcji krawędzi metodą Canny
cv.createTrackbar("LowThreshold", "TrackingImage", 0, 255, valueLow)
cv.createTrackbar("HighThreshold", "TrackingImage", 0, 255, valueHigh)
#pętla umożliwiająca ciągłe działanie programu
while(True):
    #odczyt z kamer przetworzony na odpowiednie dane
    return_value, image = camera.read()
    #zmienne określanące wartość położenia paska śledzenia
    h=cv.getTrackbarPos("HighThreshold","TrackingImage")
    l=cv.getTrackbarPos("LowThreshold","TrackingImage")
    #zastosowanie detekcji krawędzi na obrazie wejściowym kamery
    image = cv.Canny(image, l, h)
    # przedstawienie wyników metody Canny w oknie o nazwie Image, oraz stworzenie miejsca dla pasków śledzenia
    cv.imshow("Image", image)
    cv.imshow("TrackingImage", img)
    #wykorzystanie klawisza "Esc" do zamknięcia działania programu
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
#zamknięcie wszystkich okien
cv.destroyAllWindows()