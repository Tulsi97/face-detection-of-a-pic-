import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
scale_factor = 2.5

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scale_factor, 5)
    for(fx, fy, fw, fh ) in faces:
        cv2.rectangle(frame, (fx,fy), (fx+fw, fy+fh), (255,0,0), 2)
        roi_gray = gray[fy:fy+fh, fx:fx+fw]
        roi_color = frame[fy:fy+fh, fx:fx+fw]
        
        eyes =eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,255), 2)
            
        cv2.imshow('frame', frame)
        if cv2.waitKey(30) ==27:
            break
        
cap.release()
cv2.destroyAllWindows()        

