import cv2
from cv2 import cv2
import time
cap=cv2.VideoCapture(0)

while cap.isOpened():
    ret, back=cap.read()
    if ret:
        cv2.imshow("image",back)
        if cv2.waitKey(5)==ord('q'):
            cv2.imwrite('image.jpg',back)
            break
cap.release()
cv2.destroyAllWindows()        




