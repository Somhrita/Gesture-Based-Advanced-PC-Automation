import cv2
import numpy as np
from tkinter import *
import tkinter as tk

from PIL import Image, ImageTk

# Load HAAR face classifier
face_classifier = cv2.CascadeClassifier(r'C:\Users\USER\Desktop\v_auto\Virtual-Mouse\Unlock-Application\Haarcascades\haarcascade_frontalface_default.xml')
root=Tk()

root.geometry("900x520")
root.configure(bg='black')
app=tk.Frame(root,height=500,width=850,bg='black',bd=5)
app.pack()
app.grid_rowconfigure(0, minsize = 600)
app.grid_columnconfigure(0, minsize = 1000)
l1=tk.Label(app,bg='red',borderwidth=5,relief='raised')
l1.place(x=350,y=70)
label= tk.Label(app,text='FACE IMAGE TAKING',font=("times new roman",15,'bold'),fg='black')
label.place(x=100,y=400)
root.maxsize(900,520)

# Load functions
def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    if faces is ():
        return None
    
    # Crop all faces found
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face

# Initialize Webcam
cap = cv2.VideoCapture(1)
count = 0
import os
 
dir = r'C:\Users\USER\Desktop\v_auto\Virtual-Mouse\facedata'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

# Collect 100 samples of your face from webcam input
while True:
    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame), (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        img = ImageTk.PhotoImage(Image.fromarray(face))
        l1['image']=img
        label['text']=count
        # Save file in specified directory with unique name
        
        file_name_path = 'C:\\Users\\USER\\Desktop\\v_auto\\Virtual-Mouse\\facedata\\' + str(count) + '.jpg'
        cv2.imwrite(file_name_path, face)

        # Put count on images and display live count

        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        root.update()
        
    else:
        print("Face not found")
        pass

    if cv2.waitKey(1) == 13 or count ==400 : #13 is the Enter Key
        break
        
cap.release()
cv2.destroyAllWindows()      
print("Collecting Samples Complete")