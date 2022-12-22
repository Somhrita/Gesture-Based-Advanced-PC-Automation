import keyboard
from win10toast import ToastNotifier
import os
import tkinter as tk
# toast=ToastNotifier()
# toast.show_toast(
#     "Attention  !", "Gesture automation has been started", duration=10)

def select_action():
    
     def ok():
         global file

         #print("value is", var.get())
         file = var.get()
        
         master.destroy()

     OPTIONS = ['Vir-automate','Vir-mouse']

     master = tk.Tk()
     master.title("Select Action")
     master.geometry("250x200")
     var = tk.StringVar(master)
     var.set(OPTIONS[0])  # initial value

     option = tk.OptionMenu(master, var, *OPTIONS)
     option.pack()

     button = tk.Button(master, text="OK", command=ok)
     button.pack()
     
     tk.mainloop()

while True:
    try:
        #lock screen code....
        if keyboard.is_pressed("ctrl+8"):
            select_action()

            select=''
            if file =='Vir-automate':
                select="python automate.py"
            elif file=="Vir-mouse":
                select="python handtracker.py"
            print(select)
            os.system(select)

            # exec(open("lockscreen.py").read())
    except:
        continue
