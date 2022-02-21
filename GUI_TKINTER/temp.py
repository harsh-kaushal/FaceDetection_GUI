import tkinter
from tkinter import *
import PIL
from PIL import Image, ImageTk

import time

#######################################################################################################################

def cap_screen():
    capturing_screen = Toplevel()
    capturing_screen.title("capturing_screen")
    capturing_screen.geometry("800x480+0+0")
    capturing_screen.overrideredirect(False) #Set this to true to disable minimize/exit bar


    #Blank Blocks : Only for astherics
    blank1 =Label(capturing_screen,text=" ",pady=10)
    blank1.grid(row =1,column =0,columnspan=8) #Blank Row below Org name

    blank2 =Label(capturing_screen,text=" ",pady=30)
    blank2.grid(row =8,column =0,columnspan=8) #Blank Row below photo and instructions

    blank3 =Label(capturing_screen,text=" ",pady=20)
    blank3.grid(row =9,column =0,columnspan=8,rowspan=2) #Blank Row between instructions and bottom text

    #blank4 =Label(capturing_screen,text="",padx=10)
    #blank4.grid(row =1,column =0,rowspan=7) #Blank Column on left

    #blank5 =Label(capturing_screen,text="",padx=10)
    #blank5.grid(row =1,column =7,rowspan=7) #Blank Column on right



    #AT Bottom
    status= Label(capturing_screen,text="Developed In Delhi Technological University",bd = 1 ,relief=SUNKEN,anchor=E)
    status.grid(row=11,column =0 ,columnspan=8,sticky=W+E)


    #Organization Name Placement
    orgnameframe= LabelFrame(capturing_screen,padx=95,pady=15)
    orgnameframe.grid(row=0,column=0,columnspan=8)

    org_name = Label(orgnameframe,text = "Delhi Technological University",anchor=CENTER)  
    org_name.config(font=("Courier", 25))
    org_name.pack()


    #Captured Photo Placement
    capturedframe = LabelFrame(capturing_screen,padx=10,pady=10)
    capturedframe.grid(row=2,column=0,rowspan=3,columnspan=2)

    image =Label(capturedframe,image = CapImg)
    image.pack()

    capturedImgLabel = Label(capturing_screen,text="              Captured Image")
    capturedImgLabel.grid(row=6,column=0,rowspan=3)



    #Database Photo Placement
    databaseframe = LabelFrame(capturing_screen,padx=10,pady=10)
    databaseframe.grid(row=2,column=6,rowspan=3,columnspan=2)


    image =Label(databaseframe,image = RecImg)
    image.pack()

    capturedImgLabel = Label(capturing_screen,text="               DataBase Image")
    capturedImgLabel.grid(row=6,column=6,rowspan=3)



    #Instructions 
    instLabel = Label(capturing_screen,text =" Please wait matching in Database ",anchor=CENTER)
    instLabel.config(font=("Courier", 15))
    instLabel.grid(row=9,column=0,columnspan=8)

    t1 = time.perf_counter()

    if i ==1:
        time.sleep(2)
        capturing_screen.destroy()
        print(t1- time.perf_counter())
        print("Destroyed in call_capturing_screen fucntion")

###########################################################################################

def call_capturing_screen():
    cap_screen()

###########################################################################################


ideal_screen = Tk()
ideal_screen.title("ideal_screen")
ideal_screen.geometry("800x480+0+0")
ideal_screen.overrideredirect(False) #Set this to true to disable minimize/exit bar


path_rec_img = "/home/jacksparrow/Desktop/Final_Fusion/Data Folder/Recieved Image/Resized1.jpg"
path_cap_img = "/home/jacksparrow/Desktop/Final_Fusion/Data Folder/Sent Image/TempImg.jpg"
path_logo ="/home/jacksparrow/Desktop/Final_Fusion/icon.jpg"



RecImg = ImageTk.PhotoImage(Image.open(path_rec_img))
CapImg = ImageTk.PhotoImage(Image.open(path_cap_img))
LogoImg = ImageTk.PhotoImage(Image.open("/home/jacksparrow/Desktop/icon.jpg"))


global i

i=0



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


#Organization Photo Placement
photoframe = LabelFrame(ideal_screen,padx=0,pady=0)
photoframe.grid(row=2,column=3,rowspan=3,columnspan=2)


image =Label(photoframe,image = LogoImg)
image.pack()


#Instructions 
instLabel = Label(ideal_screen,text =" Please Stand At Least 1 meter away from the camera ",anchor=CENTER)
instLabel.config(font=("Courier", 15))
instLabel.grid(row=7,column=3)



ideal_screen.after(3000,call_capturing_screen)


mainloop()