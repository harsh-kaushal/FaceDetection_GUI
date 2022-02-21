import tkinter
from tkinter import *
import PIL
from PIL import Image, ImageTk

import tkinter.ttk as *



root = Tk()
root.title("ROOT")
root.geometry("800x480+0+0")
root.overrideredirect(False) #Set this to true to disable minimize/exit bar

s=ttk.Style()
s.theme_use('alt')


for i in [0,1,2,3,4,5]:
    for j in [0,1,2,3,4,5,6,7]:
        gridframe = LabelFrame(root,padx=30,pady=25)
        gridframe.grid(row=i,column=j)
        staticLabel = Label(gridframe,text = str(i) +" x " + str(j) ) 
        staticLabel.pack() 







root.mainloop()