import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('kartu1.png')  # Menyimpan gambar dari file
img = cv2.imread('kartu2.png')
img = cv2.imread('barcode1.jpeg')
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

with open('myDataFile.txt') as f:
    myDataList = f.read().splitlines()

while True:
    success, img = cap.read()  # Mengambil gambar dari webcam
    if not success:  
        break
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList:
            myOutput = 'Terdaftar'
            myColor = (0, 255, 0)
        else:
            myOutput = 'Tidak Terdaftar'
            myColor = (0, 0, 255)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 5)
        pts2 = barcode.rect
        cv2.putText(img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, myColor, 2)

    cv2.imshow('Result', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
