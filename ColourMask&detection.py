import cv2
import numpy as np
from datetime import datetime

video =cv2.VideoCapture(0)
photo_counter = 0
while True:
    orig_frame =cv2.imread("test4.jpg")
    #if not ret:
    #    video = cv2.VideoCapture(0)
     #   continue

    frame = cv2.GaussianBlur(orig_frame, (3, 3), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_yellow = np.array([100, 50, 50])
    up_yellow = np.array([120, 255, 100])
    mask = cv2.inRange(hsv, low_yellow, up_yellow)
    edges = cv2.Canny(mask, 75, 150)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours2 = cv2.drawContours(edges, contours, -1, (115, 239, 236),2)
    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)

    key = cv2.waitKey(25)

    if key & 0xFF == ord('s'):
        photo_counter += 1
        photo_capture_time = datetime.now().strftime('%d.%m.%Y-%H.%M.%S')
        photo_name = f'{photo_counter}-zdjecie-{photo_capture_time}.jpg'
        edge_name = f'{photo_counter}-krawedz-{photo_capture_time}.jpg'
        cv2.imwrite(photo_name, frame)
        cv2.imwrite(edge_name, edges)
        print(photo_capture_time, ': ', photo_counter, '. photo captured.', sep='')
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()