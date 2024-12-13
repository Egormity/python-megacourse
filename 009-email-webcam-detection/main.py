import cv2
import glob
import os 
import threading
from email  import send_email

capture = cv2.VideoCapture(0)

first_frame = None
status_list = []
count = 1

def clean_folder():
    images = glob.glob("images/*")
    for image in images:
        os.remove(image)

while True:
    status = 0
    check, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_gau = cv2.GaussianBlur(gray, (21, 21), 0)
    if first_frame is None:
        first_frame = gray_gau

    delta_frame = cv2.absdiff(first_frame, gray_gau)
    cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(delta_frame, None, iterations=2)
    contours, _ = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rect = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        if rect.any(): 
            status = 1
            cv2.imwrite(f"/images/{count}.png", frame)
            count += 1
            image_email = f"/images/{int(count / 2)}.png"

    status_list.append(status)
    status_list = status_list[-2:]
    
    if status_list[0] == 1 and status_list[-2] == 0:
        def func ():
            send_email(image_email)
            clean_folder()
        thread = threading.Thread(target=func).start()

    cv2.imshow('frame', contours)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()