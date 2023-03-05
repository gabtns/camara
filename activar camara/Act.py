import cv2
import numpy as np

images = cv2.imread("camara_\wally.jpg")
gris = cv2.cvtColor(images,cv2.COLOR_BGR2GRAY)
template = cv2.imread("camara_\wally2.png",0)
w , h = template.shape[::-1]

res = cv2.matchTemplate(gris, template, cv2.TM_CCOEFF_NORMED)

umbral = 0.2
rectangulos = np.where(res >= umbral)

for i in zip(*rectangulos[::-1]):
    print(i)
    cv2.rectangle(images, i, (i[0] + w, i[1] + h), (0,255,0),1)

cv2.namedWindow("resultado",cv2.WINDOW_NORMAL)   
cv2.imshow("resultado",images )

cv2.waitKey()
cv2.destroyAllWindows()
