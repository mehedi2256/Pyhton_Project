from tkinter import *
from customtkinter import  *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import os

root = Tk()
root.title("White Board by Mehedi")
root.geometry("1050x570+150+50")
root.config(bg="#f2f3f5")
root.resizable(False,False)

current_x = 0
current_y = 0
color="black"

def locate_xy(work):
    global current_x,current_y

    current_x = work.x
    current_y = work.y
def addline(work):
    global current_x,current_y

    canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),
            fill = color,capstyle=ROUND,smooth=True)
    current_x,current_y = work.x,work.y

def show_color(new_color):
    global color

    color = new_color

def new_canvas():
    canvas.delete('all')
    display_pallete()

def insertimage():
    global filename
    global f_img
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image file",
                filetypes=(("PNG file","* .png"),("All file","new.txt")))

    f_img = tk.PhotoImage(file=filename)
    my_img = canvas.create_image(180,50,image=f_img)
    root.bind("<B3-Motion>",my_callback)

def my_callback(event):
    global f_img
    f_img = tk.PhotoImage(file=filename)
    my_img = canvas.create_image(event.x,event.y,image=f_img)

#icons section
image_icon = PhotoImage(file="mehedi_logo.png")
root.iconphoto(False,image_icon)

# sidebar section
color_box = Canvas(root,bg="floral white",width=40,height=480,bd=0)
color_box.place(x=29,y=20)

eraser = PhotoImage(file="eraser.png")
Button(root,image=eraser,bg="#f2f3f5",command=new_canvas).place(x=36,y=410)

import_image = PhotoImage(file="addimage.png")
Button(root,image=import_image,bg="white",command=insertimage).place(x=36,y=460)

#clors
colors=Canvas(root,bg="floral white",width=37,height=300,bd=0)
colors.place(x=30,y=60)

def display_pallete():
    id = colors.create_rectangle((10,10,30,30),fill="brown")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('brown'))

    id = colors.create_rectangle((10, 40, 30, 60), fill="black")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

    id = colors.create_rectangle((10,70,30,90),fill="white")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('white'))

    id = colors.create_rectangle((10,100,30,120),fill="yellow")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('yellow'))

    id = colors.create_rectangle((10,130,30,150),fill="red")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('red'))

    id = colors.create_rectangle((10,160,30,180),fill="orange")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('orange'))

    id = colors.create_rectangle((10,190,30,210),fill="green")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('green'))

    id = colors.create_rectangle((10,220,30,240),fill="blue")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('blue'))

    id = colors.create_rectangle((10,250,30,270),fill="purple")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('purple'))

display_pallete()


#main screen
canvas = Canvas(root,width=930,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=10)

canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>',addline)

#slider
current_value = tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())
slider = ttk.Scale(root, from_=0,to=100,orient="horizontal",command=slider_changed,variable=current_value )
slider.place(x=30,y=530)

value_label = ttk.Label(root,text=get_current_value())
value_label.place(x=27,y=550)


root.mainloop()