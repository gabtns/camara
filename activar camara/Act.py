import cv2 

def abrir():
    conteo = 0
    cap = cv2.VideoCapture(0)
    while (cap.isOpened()):
        ret,frame = cap.read()

        cv2.imshow("capturas",frame)
        conteo+=1
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()   


abrir()    
