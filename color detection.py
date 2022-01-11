from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from kmean import nameit
from percent import percentage
import cv2
from contour import con
from shape import shapedet
import os

root = Tk()
root.title("Colour Detection")
root.geometry("550x300")
root.resizable(width = True, height = True)

def colours():
    n = int(num.get())
    nameit(x,n)

def percent():
    root2 = Toplevel(root1)
    root2.title("Percentage of each colour")
    root2.geometry("550x300")
    m = int(num.get())
    per = percentage(x,m)
    #print(per)
    #print(len(per))
    key = list(per.keys())
    value = list(per.values())
    t = Text(root2)
    #print(m)
    #print(len(value))
    for i in range(0,len(value)):
        #print(i)
        s = "{:.3f}".format(value[i])
        s1 = str(s)
        s2 = str(key[i])
        t.insert(END, s2 + "\t\t\t\t\t\t\t" + s1 + "%\n")
    t.pack()

def sort():
    root3 = Toplevel(root1)
    root3.title("Maximum and Minimum Colors")
    root3.geometry("550x300")
    mn = int(num.get())
    sor = percentage(x,mn)
    sor1 = sorted(sor.items(),key = lambda x:x[1])
    min1 = sor1[0][0]
    min2 = "{:.3f}".format(sor1[0][1])
    s = str(min2)
    max1 = sor1[mn-1][0]
    max2 = "{:.3f}".format(sor1[mn-1][1])
    s1 = str(max2)
    t1 = Text(root3)
    t1.insert(END, "Minimum Color: "+ min1 + "\t\t\t\t\t\t\t" + s +"%\nMaximum Color: " + max1 + "\t\t\t\t\t\t\t" + s1 + "%")
    t1.pack()

def shap():
    shapedet(x)
    #exec('scroll.py')

def drawc():
    con(x)

def km():
    global root1
    root1 = Toplevel(root)
    root1.title("Colours Detected")
    root1.geometry("500x500")
    btn1 = Button(root1, text ='Color Detected', command = colours, width = 50, height = 5)
    btn1.pack()
    btn2 = Button(root1, text ='Percentage of Color Detected', command = percent, width = 50, height = 5)
    btn2.pack()
    btn3 = Button(root1, text ='Colours Present maximum and minimum', command = sort, width = 50, height = 5)
    btn3.pack()
    btn8 = Button(root1, text ='Draw Contours', command = drawc, width = 50, height = 5)
    btn8.pack()
    btn9 = Button(root1, text ='Shape Detection', command = shap, width = 50, height = 5)
    btn9.pack()

def cap(img_name):
    ca = cv2.imread(img_name)
    ca1 = cv2.cvtColor(ca, cv2.COLOR_BGR2RGB)
    ca3 = Image.fromarray(ca1)
    im1 = ca3.resize(( 950, 750), Image.ANTIALIAS)
    im1 = ImageTk.PhotoImage(ca3)
    panel = Label(root, image = im1)
    panel.image = im1
    panel.grid(row = 2)
    global num
    num = Entry(root)
    num.place(x = 1000, y = 150)
    btn7 = Button(root,text="Set Clusters",command=km)
    btn7.place(x = 1000, y = 200)

def captured(ima):
    global x
    x = "D:/Documents/Desktop/DRDO_Project/opencv_frame_.png"
    ca2 = cv2.cvtColor(ima, cv2.COLOR_BGR2RGB)
    cv2.imwrite(x, ca2)
    cap(x)

def web():
    #im = None
    win = Toplevel(root)
    win.geometry("700x700")
    label =Label(win)
    label.grid(row=0, column=0)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def show_frames():
        # im = None
        im = cap.read()[1]
        #print(im)
        global cv2image
        cv2image= cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        #print(cv2image)
        #global img
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image = img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        label.after(20, show_frames)
       
    show_frames()
    btn6 = Button(win, text = 'Capture', command = lambda:captured(cv2image), width = 40, height = 5)
    btn6.place(x = 200, y = 500)
    win.mainloop()

def open_img():
    global x
    x = filedialog.askopenfilename(title ='Open File')
    img = Image.open(x)
    img1 = img.resize(( 950, 750), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    panel = Label(root, image = img1)
    panel.image = img1
    panel.grid(row = 2)
    global num
    num = Entry(root)
    num.place(x = 1000, y = 150)
    btn4 = Button(root,text="Set Clusters",command=km)
    btn4.place(x = 1000, y = 200)

btn = Button(root, text = 'Open Image', command = open_img)
btn.place(x = 1000, y = 50)
btn5 = Button(root, text = 'Image using Webcam', command = web)
btn5.place(x = 1000, y = 100)
root.mainloop()