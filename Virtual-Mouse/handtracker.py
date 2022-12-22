import cv2
import mediapipe
import numpy
import pyautogui
import autopy
import keyboard
import tkinter as tk 
# import win32gui,win32con
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
cap = cv2.VideoCapture(int(channel))

initHand = mediapipe.solutions.hands

mainHand = initHand.Hands(min_detection_confidence=0.9, min_tracking_confidence=0.7)
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
    check, img = cap.read()  # Reads frames from the camera
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Changes the format of the frames from BGR to RGB
    lmList = handLandmarks(imgRGB)


    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]  # Gets index 8s x and y values (skips index value because it starts from 1)
        x2, y2 = lmList[12][1:]  # Gets index 12s x and y values (skips index value because it starts from 1)
        finger = fingers(lmList)  # Calling the fingers function to check which fingers are up
        print(finger)

        if finger[0] == 1 and finger[1] == 1 and finger[2]==0 and finger[3]==0 and finger[4]==0:  # Checks to see if the pointing finger is up and thumb finger is down
            x3 = numpy.interp(x1, (75, 640 - 75), (0, wScr))
            y3 = numpy.interp(y1, (75, 480 - 75), (0, hScr))

            cX = pX + (x3 - pX) / 7
            cY = pY + (y3 - pY) / 7

            autopy.mouse.move(wScr-cX, cY)  # Function to move the mouse to the x3 and y3 values (wSrc inverts the direction)
            pX, pY = cX, cY

        if finger[0] == 0 and finger[1] == 1 and finger[2]==0 and finger[3]==0 and finger[4]==0:  # Checks to see if the pointer finger is down and thumb finger is up
            autopy.mouse.click()  # Left click

        if finger[0] == 0 and finger[1] == 1 and finger[2]==1 and finger[3]==0 and finger[4]==0:
            pyautogui.doubleClick() # double click
        if finger[0] == 1 and finger[1] == 0 and finger[2]==0 and finger[3]==0 and finger[4]==0:
            pyautogui.scroll(150) # scroll up
        if finger[0] == 0 and finger[1] == 0 and finger[2]==0 and finger[3]==0 and finger[4]==1:
            pyautogui.scroll(-150) #scroll down





    
    # os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "python" to true' ''')
    if cv2.waitKey(1) and keyboard.is_pressed('ctrl+k'):
        cap.release()
        cv2.destroyAllWindows()
        break