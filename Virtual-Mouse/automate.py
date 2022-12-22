

import pickle
import cv2
import keyboard
import mediapipe
import time
import pyautogui
import autopy
import numpy
import os
import ctypes
import uuid
from pynput.keyboard import Key, Controller
import win32gui,win32con


keyBoard=Controller()
pyautogui.FAILSAFE = False
user=ctypes.windll.User32
# window_handle=FindWindow(None,'D')


import tkinter as tk
import cv2
import pickle
def returnCameraIndexes():
    # checks the first 10 indexes.
    index = 0
    arr = []
    i = 10
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    return arr

# clicked.set()
lst=(returnCameraIndexes())
lst=list(map(str,lst))

# --- functions ---

def select_channel():

     def ok():
         global channel

         #print("value is", var.get())
         channel = var.get()

         master.destroy()

     OPTIONS = lst

     master = tk.Tk()
     master.title("Select Camera")
     master.geometry("250x200")
     var = tk.StringVar(master)
     var.set(OPTIONS[0])  # initial value

     option = tk.OptionMenu(master, var, *OPTIONS)
     option.pack()

     button = tk.Button(master, text="OK", command=ok)
     button.pack()

     tk.mainloop()

# --- main ---

select_channel()
# dict_map={"ch":channel}
# file=open("Original.txt","wb")
# pickle.dump(dict_map, file)
# file.close()



cap = cv2.VideoCapture(int(channel))


cap.set(cv2.CAP_PROP_FRAME_HEIGHT,900)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,900)
initHand = mediapipe.solutions.hands

mainHand = initHand.Hands(min_detection_confidence=0.6, min_tracking_confidence=0.5)
draw = mediapipe.solutions.drawing_utils
wScr, hScr = autopy.screen.size()
pX, pY = 0, 0
cX, cY = 0, 0


def handLandmarks(colorImg):
    landmarkList = []

    landmarkPositions = mainHand.process(colorImg)
    landmarkCheck = landmarkPositions.multi_hand_landmarks
    if landmarkCheck:
        for hand in landmarkCheck:
            for index, landmark in enumerate(hand.landmark):
                draw.draw_landmarks(img, hand, initHand.HAND_CONNECTIONS)
                h, w, c = img.shape
                centerX, centerY = int(landmark.x * w), int(landmark.y * h)
                landmarkList.append([index, centerX, centerY])
                
    return landmarkList


def fingers(landmarks):
    fingerTips = []
    tipIds = [4, 8, 12, 16, 20]
    
    # Check if thumb is up
    if landmarks[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
        fingerTips.append(1)
    else:
        fingerTips.append(0)
    
    # Check if fingers are up except the thumb
    for id in range(1, 5):
        if landmarks[tipIds[id]][2] < landmarks[tipIds[id] - 3][2]:
            fingerTips.append(1)
        else:
            fingerTips.append(0)

    return fingerTips


while True:
    try:
        
        check, img = cap.read()  # Reads frames from the camera
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Changes the format of the frames from BGR to RGB
        lmList = handLandmarks(imgRGB)


        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]  # Gets index 8s x and y values (skips index value because it starts from 1)
            x2, y2 = lmList[12][1:]  # Gets index 12s x and y values (skips index value because it starts from 1)
            finger = fingers(lmList)  # Calling the fingers function to check which fingers are up
            print(finger)

            if finger[0] == 0 and finger[1] == 0 and finger[2]==0 and finger[3]==0 and finger[4]==0:
                
                #356 x 334
                time.sleep(1)
                pyautogui.click(x=356,y=334)
                pyautogui.keyDown('alt')
                pyautogui.keyDown('f4')
                pyautogui.keyUp('f4')
                pyautogui.keyUp('alt')                             #[0 0 0 0 0]
                pyautogui.click(x=704,y=396)
                
                
            if finger[0] == 1 and finger[1] == 1 and finger[2]==0 and finger[3]==0 and finger[4]==0:  # Checks to see if the pointing finger is up and thumb finger is down
                
                pyautogui.press("volumeup")
                
            if finger[0] == 0 and finger[1] == 1 and finger[2]==0 and finger[3]==0 and finger[4]==0:  # Checks to see if the pointer finger is down and thumb finger is up
                pyautogui.press('volumedown')
                
            if finger[0] == 1 and finger[1] == 1 and finger[2]==1 and finger[3]==0 and finger[4]==0:
                time.sleep(1)  # Checks to see if the pointer finger is down and thumb finger is up
                pyautogui.press('space')    

                                                                            #[0 1 0 0 0 ]
                
            if finger[0] == 0 and finger[1] == 1 and finger[2]==1 and finger[3]==0 and finger[4]==0:
                try:
                #task2
                    x1,y1=pyautogui.locateCenterOnScreen("C:/Users/USER/Desktop/v_auto/file.png",grayscale=True,confidence=.5)
                    pyautogui.click(x1,y1)
                    # pyautogui.moveTo(100,100,1)
                    time.sleep(1)
                    x2,y2=pyautogui.locateCenterOnScreen("C:/Users/USER/Desktop/v_auto/saveas.png",grayscale=False,confidence=.5)
                    pyautogui.click(x2,y2)
                    time.sleep(1)
                    pyautogui.click(261,396)
                    time.sleep(1.5)

                    pyautogui.keyDown('win')
                    pyautogui.keyDown('c')
                    pyautogui.keyUp('c')
                    pyautogui.keyUp('win')

                    x3,y3=pyautogui.locateCenterOnScreen("C:/Users/USER/Desktop/v_auto/dialog1.png",grayscale=False,confidence=.5)
                    pyautogui.click(x3,y3)
                    path=r"C:\Users\USER\Desktop\Automate files"
                    file_text=str(uuid.uuid1())[:8]
                    pyautogui.write(path,interval=0.010)
                    time.sleep(1)
                    # 
                    x4,y4=pyautogui.locateCenterOnScreen("C:/Users/USER/Desktop/v_auto/arrow.png",grayscale=False,confidence=.5)
                    pyautogui.click(x4,y4)
                    time.sleep(1)

                    x5,y5=pyautogui.locateCenterOnScreen("C:/Users/USER/Desktop/v_auto/filename.png",grayscale=False,confidence=.5)
                    
                    pyautogui.click(x5,y5)
                    pyautogui.write(file_text)
                    x6,y6=pyautogui.locateCenterOnScreen("C:/Users/USER/Desktop/v_auto/save.png",grayscale=False,confidence=.5)
                    pyautogui.click(x6,y6)

                                                                                #   [0 1 1 0 0]
                
                    
                except:
                    continue
                # pyautogui.click(x2,y2)
            if finger[0] == 1 and finger[1] == 0 and finger[2]==0 and finger[3]==0 and finger[4]==0:
                # pass
                pyautogui.scroll(150) # scroll up                                  #[1 0 0 0 0]
            if finger[0] == 0 and finger[1] == 0 and finger[2]==0 and finger[3]==0 and finger[4]==1:
                # pass
                pyautogui.scroll(-150) #scroll down                                #[0 0 0 0 1]
            if finger[0] == 0 and finger[1] == 1 and finger[2]==0 and finger[3]==0 and finger[4]==1:
                # pass
                    pyautogui.keyDown('ctrl')
                    pyautogui.keyDown('p')
                    pyautogui.keyUp('p')
                    pyautogui.keyUp('ctrl')                                     #[0 1 0 0 1]
            # if finger[0] == 0 and finger[1] == 1 and finger[2]==1 and finger[3]==1 and finger[4]==1:
            #                 os.system('shutdown -t 1 -r -f')                   #[0 1 1 1 1]
            if finger[0] == 0 and finger[1] == 1 and finger[2]==1 and finger[3]==1 and finger[4]==0:
                
                ctypes.windll.user32.LockWorkStation()
        # elif user.GetForegroundWindow()%10==0:
        #         print('locked')
        #         keyBoard.press(Key.space)
        #         keyBoard.release(Key.space)
                
                      
    except:
        continue                   
    cv2.namedWindow('VIR_MATE', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('VIR_MATE',400,300) 
    cv2.imshow("VIR_MATE",img)
    hWnd = win32gui.FindWindow(None, 'VIR_MATE')
    win32gui.SetWindowPos(hWnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
    # Creates a window
    # os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "python" to true' ''')
    if cv2.waitKey(1) and keyboard.is_pressed('ctrl+k'):
        cap.release()
        cv2.destroyAllWindows()
        break
   
# after break, control goes here...
#execute lockscreen
# exec(open("lockscreen.py").read())