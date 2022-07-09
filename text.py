"""
GUI for Rover Arm Control System
Started on - 25th July 2022
Working - Helps to control the working of the arm.
"""

# Import required Libraries
from tkinter import *
from PIL import Image, ImageTk
import cv2
from time import strftime
from datetime import date, datetime
from random import randint
from tkinter import ttk, messagebox
from tkinter import ttk


# Create an instance of TKinter Window or frame
window = Tk()

# Set the size of the window
window.geometry("1400x800")
window.title("Control System")
window.configure(bg="white")



# window.geometry("1535x863") ------ my pc resolutuion

'''To get your Monitor's width'''
#screen_width = window.winfo_screenwidth()

'''To get your Monitor's height'''
#screen_height = window.winfo_screenheight()

'''Inserting values'''
# size=str(screen_width)+'x'+str(screen_height)
# window.geometry(size)


'''Make window Non-Resizable'''
window.resizable(0, 0)

''' Remove maximize,minimize,cancel buttons'''
# window.overrideredirect(True)


'''Images Used'''
icon = PhotoImage(file="images/icon1.png")
left = PhotoImage(file="images/left.png")
right = PhotoImage(file="images/right.png")
top = PhotoImage(file="images/top.png")
bottom = PhotoImage(file="images/bottom.png")
window.iconphoto(False, icon)
change_camera = PhotoImage(file="images/Change_cam.png")

# For vedio Streaming (Camera)
global cam,ch,x,y,z

ch,x,y,z=0,0,0,0
cam= cv2.VideoCapture(0)


# Define function to show frame
def vedio_stream():
   global cam
   try:
      # Get the latest frame and convert into Image
      cv2image= cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2RGB)
   except Exception as e:
      messagebox.showwarning("Error.!", e)
      cam= cv2.VideoCapture(0)
      cv2image= cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2RGB)

   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   camera.imgtk = imgtk
   camera.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   camera.after(10, vedio_stream)

#To chnage the camera
def changeCamera():
   global cam,ch
   if(ch==0):
      cam= cv2.VideoCapture(1)
      ch=1
   else:
      cam= cv2.VideoCapture(0)
      ch=0

#To click Picture  
def clickpic():  
   now = datetime.now()
   time = now.strftime("%M%S")
   check, frame = cam.read()
   string = str(date.today())+str(time)+"file.jpg"
   cv2.imwrite(filename=string, img=frame)
   messagebox.showinfo("Success.!", "Image saved!")


def upward():
   global x
   x=x+10
   x_cord.delete(0, END)
   x_cord.insert(0,x)

def backward():
   global y
   y=y+10
   y_cord.delete(0, END)
   y_cord.insert(0,y)

def leftward():
   global x,z,y
   z=z+10
   z_cord.delete(0, END)
   z_cord.insert(0,z)

   y=y+5
   y_cord.delete(0, END)
   y_cord.insert(0,y)

   x=x+6
   x_cord.delete(0, END)
   x_cord.insert(0,x)

#Camera Border
camera_border=Label(window,height="19",width="40",bg="yellow")
camera_border.place(relx=.05,rely=.06)



# Create a Label to capture the Video frames
camera=Label(camera_border,height="260",width="260")
camera.place(relx=.025,rely=.049)


camchange_btn = Button(window,text="Change Camera",font=("Bahnschrift", 12) ,cursor="hand2",bd=1,bg="blue",fg="White",relief="raised",
activebackground = "yellow",command=changeCamera)
camchange_btn.place(relx=.06, rely=.010)

clickphoto_btn = Button(window,text="Click Picture",font=("Bahnschrift", 12) ,cursor="hand2",bd=1,bg="blue",fg="White",relief="raised",
activebackground = "yellow",command=clickpic)
clickphoto_btn.place(relx=.16, rely=.010)



#For Control Label -----
control_lbl = Label(window, text="CONTROLS", font=("Bahnschrift", 45, "bold"), bg='white', fg='blue')
control_lbl.place(x=60, y=380)


#control button ----
left_btn = Button(window,image=left,cursor="hand2",bg="white",activebackground="white",bd=0,relief="raised",command=leftward)
left_btn.place(x=50,y=550)

right_btn = Button(window,image=right,cursor="hand2",bg="white",activebackground="white",bd=0,relief="raised")
right_btn.place(x=250,y=550)

top_btn = Button(window,image=top,cursor="hand2",bg="white",activebackground="white",bd=0,relief="raised",command=upward)
top_btn.place(x=150,y=470)

bottom_btn = Button(window,image=bottom,cursor="hand2",bg="white",activebackground="white",bd=0,relief="raised",command=backward)
bottom_btn.place(x=150,y=640)

box1frame = LabelFrame(window, text="", bg="silver", width=950, height=700, bd=0)
box1frame.place(x=400, y=10)

box3frame = LabelFrame(window, text="", bg="white", width=950, height=20, bd=0)
box3frame.place(x=400, y=530)

box2frame = LabelFrame(window, text="", bg="red", width=950, height=70, bd=0)
box2frame.place(x=400, y=725)

#Other task button ----
Handges_btn = Button(window,text="Hand Gestures",font=("Helvetica", 20) ,cursor="hand2",bd=1,bg="blue",fg="White",relief="raised",
activebackground = "yellow")
Handges_btn.place(x=500,y=735)

SwitchingTask_btn = Button(window,text="Switching Task",font=("Helvetica", 20) ,cursor="hand2",bd=1,bg="blue",fg="White",relief="raised",
activebackground = "yellow")
SwitchingTask_btn.place(x=800,y=735)

STOP_btn = Button(window,text="STOP",font=("Helvetica", 18) ,cursor="hand2",bd=5,bg="RED",fg="White",relief="raised",
activebackground = "yellow",command=quit)
STOP_btn.place(x=1100,y=735)



#Main Box---------------------------

picklabel = Label(box1frame, text="Pick Position", font=("Bahnschrift", 23,"bold"), bg='silver', fg='blue')
picklabel.place(x=400, y=10)

picdlabel = Label(box1frame, text="Input The Coordinates Of Desired Position Below", font=("Bahnschrift", 15,"italic"), bg='silver', fg='blue')
picdlabel.place(x=280, y=50)

piccdlabel = Label(box1frame, text="X                                                                  Y                                                               Z", font=("Bahnschrift", 15,"italic"), bg='silver', fg='blue')
piccdlabel.place(x=130, y=80)

piccdlabeelll= Label(box1frame, text="Cm                                                           Cm                                                          Cm", font=("Bahnschrift", 14,"italic"), bg='silver', fg='yellow')
piccdlabeelll.place(x=250, y=120)

x_cord = Entry(box1frame, width=15, bg="silver", bd=1,font=(10), fg="white")
x_cord.place(x=80, y=120)
x_cord.insert(0,x)

y_cord = Entry(box1frame, width=15, bg="silver", bd=1,font=(10), fg="white")
y_cord.place(x=400, y=120)
y_cord.insert(0,y)

z_cord = Entry(box1frame, width=15, bg="silver", bd=1,font=(10), fg="white")
z_cord.place(x=720, y=120)
z_cord.insert(0,z)



calKI_btn = Button(window,text="Calculate Inverse Kinematics",font=("Helvetica", 18) ,cursor="hand2",bd=3,bg="green",fg="White",relief="raised",
activebackground = "yellow")
calKI_btn.place(x=700,y=170)


picdlabell = Label(box1frame, text="The Angles Corresponding To Pick Position Are", font=("Bahnschrift", 15,"italic"), bg='silver', fg='blue')
picdlabell.place(x=280, y=220)


piccdlabell= Label(box1frame, text="Waist/base                                                       Shoulder                                                    Elbow", font=("Bahnschrift", 15,"italic"), bg='silver', fg='blue')
piccdlabell.place(x=70, y=260)


piccdlabelll= Label(box1frame, text="Degree                                                    Degree                                                   Degree", font=("Bahnschrift", 14,"italic"), bg='silver', fg='yellow')
piccdlabelll.place(x=250, y=300)


x_angle = Entry(box1frame, width=15, bg="silver", bd=1,font=(10), fg="white")
x_angle.place(x=80, y=300)
x_angle.insert(0,"           0")

y_angle = Entry(box1frame, width=15, bg="silver", bd=1,font=(10), fg="white")
y_angle.place(x=400, y=300)
y_angle.insert(0,"            0")

z_angle = Entry(box1frame, width=15, bg="silver", bd=1,font=(10), fg="white")
z_angle.place(x=720, y=300)
z_angle.insert(0,"             0")


sli1 = Scale(box1frame, from_=0, to=100, orient=HORIZONTAL, length= 900,bg="silver",fg="blue",bd=0)
sli1.set(50)
sli1.place(x=20,y=600)


ppicdlabell = Label(box1frame, text="Move The Slider For Gripper Jaw Movement", font=("Bahnschrift", 15,"italic"), bg='silver', fg='blue')
ppicdlabell.place(x=280, y=550)


Start_btn = Button(window,text="START",font=("Helvetica", 18) ,cursor="hand2",bd=3,bg="green",fg="White",relief="raised",
activebackground = "yellow")
Start_btn.place(x=820,y=655)






vedio_stream()
window.mainloop()