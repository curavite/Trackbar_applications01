import cv2
import numpy as np

def nothing(x):
    pass

canvas = np.zeros((512,512,3), dtype=np.uint8) # siyah tuval oluşturuyoruz

cv2.namedWindow("image") #pencere adımız

cv2.createTrackbar("R","image",0,255,nothing)
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("B","image",0,255,nothing) #tuvaller için kızakları olan trackbarlar oluşturuyoruz
cv2.createTrackbar("Switch","image",0,1,nothing)

while True:
    cv2.imshow("image", canvas)  # penceriyi görmemizi sağlar
    if cv2.waitKey(1) & 0xFF == ord("q"): # klavyeden q harfine basılınca kapanmasını sağlar
        break
    s =cv2.getTrackbarPos("Switch","image")
    r=cv2.getTrackbarPos("R","image") #trackbarın içindeki kızağın pozisyonunu çekmek için
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")

    if s==1 : #switch 1 ise kızaklarıdaki değişikler okunur
        canvas[:]=[b,g,r] #kızaklardaki alınan değerleri r g b değerlerine atamasını sağlar
    else :
        canvas[:] = [0, 0, 0]
