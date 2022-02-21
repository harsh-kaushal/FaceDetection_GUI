import tkinter
from tkinter import *
import PIL
from PIL import Image, ImageTk

#from tkinter.ttk import *

ideal_screen = Tk()
ideal_screen.title("ideal_screen")
ideal_screen.geometry("800x480+0+0")
ideal_screen.overrideredirect(False) #Set this to true to disable minimize/exit bar


#ideal_screen.style=Style()
#ideal_screen.style.theme_use("clam")


#Blank Blocks : Only for astherics
blank1 =Label(ideal_screen,text=" ",pady=10)
blank1.grid(row =1,column =0,columnspan=8) #Blank Row below Org name

blank2 =Label(ideal_screen,text=" ",pady=28)
blank2.grid(row =5,column =0,columnspan=8) #Blank Row below photo and instructions

blank3 =Label(ideal_screen,text=" ",pady=53)
blank3.grid(row =8,column =0,columnspan=8,rowspan=2) #Blank Row between instructions and bottom text

blank4 =Label(ideal_screen,text="",padx=15)
blank4.grid(row =1,column =0,rowspan=5) #Blank Column on left

blank5 =Label(ideal_screen,text="",padx=15)
blank5.grid(row =1,column =7,rowspan=5) #Blank Column on right



#AT Bottom
status= Label(ideal_screen,text="Developed In Delhi Technological University",bd = 1 ,relief=SUNKEN,anchor=E)
status.grid(row=10,column =0 ,columnspan=8,sticky=W+E)


#Organization Name Placement
orgnameframe= LabelFrame(ideal_screen,padx=95,pady=15)
orgnameframe.grid(row=0,column=0,columnspan=8)

org_name = Label(orgnameframe,text = "Delhi Technological University",anchor=CENTER)  
org_name.config(font=("Courier", 25))
org_name.pack()


#Photo Placement
photoframe = LabelFrame(ideal_screen,padx=0,pady=0)
photoframe.grid(row=2,column=3,rowspan=3,columnspan=2)

RecImg = ImageTk.PhotoImage(Image.open("/home/jacksparrow/Desktop/icon.jpg"))

image =Label(photoframe,image = RecImg)
image.pack()


#Instructions 
instLabel = Label(ideal_screen,text =" Please Stand At Least 1 meter away from the camera ",anchor=CENTER)
instLabel.config(font=("Courier", 15))
instLabel.grid(row=7,column=3)



ideal_screen.mainloop()