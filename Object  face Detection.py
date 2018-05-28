import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('ipg_group_pic.jpg')

scale_factor = 1.15

while True:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scale_factor, 5)
    for(x, y, w, h ) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255,255,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]               
            
        cv2.imshow('Image', img)
        if cv2.waitKey(30) ==27:
            break
        
cv2.destroyAllWindows()