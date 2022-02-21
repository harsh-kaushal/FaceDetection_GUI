import os
import requests
import base64
import io
import time
from cv2 import cv2
import numpy as np

import tkinter
from tkinter import *
import PIL
from PIL import Image, ImageTk

import Click_n_Crop_Fusion # Another File for Camera Use
import Communication_Fusion # Another File for Communication

#######################################################################################################################
def mat_screen():
    matching_screen = Toplevel()
    matching_screen.title("matching_screen")
    matching_screen.geometry("800x480+0+0")
    matching_screen.overrideredirect(False) #Set this to true to disable minimize/exit bar


    #Blank Blocks : Only for astherics
    blank1 =Label(matching_screen,text=" ",pady=10)
    blank1.grid(row =1,column =0,columnspan=8) #Blank Row below Org name

    blank2 =Label(matching_screen,text=" ",pady=30)
    blank2.grid(row =8,column =0,columnspan=8) #Blank Row below photo and instructions

    blank3 =Label(matching_screen,text=" ",pady=20)
    blank3.grid(row =9,column =0,columnspan=8,rowspan=2) #Blank Row between instructions and bottom text


    #AT Bottom
    status= Label(matching_screen,text="Developed In Delhi Technological University",bd = 1 ,relief=SUNKEN,anchor=E)
    status.grid(row=11,column =0 ,columnspan=8,sticky=W+E)


    #Organization Name Placement
    orgnameframe= LabelFrame(matching_screen,padx=95,pady=15)
    orgnameframe.grid(row=0,column=0,columnspan=8)

    org_name = Label(orgnameframe,text = "Delhi Technological University",anchor=CENTER)  
    org_name.config(font=("Courier", 25))
    org_name.pack()


    #Captured Photo Placement
    capturedframe = LabelFrame(matching_screen,padx=10,pady=10)
    capturedframe.grid(row=2,column=0,rowspan=3,columnspan=2)

    image =Label(capturedframe,image = CapImg)
    image.pack()

    capturedImgLabel = Label(matching_screen,text="              Captured Image")
    capturedImgLabel.grid(row=6,column=0,rowspan=3)



    #Database Photo Placement
    databaseframe = LabelFrame(matching_screen,padx=10,pady=10)
    databaseframe.grid(row=2,column=6,rowspan=3,columnspan=2)


    image =Label(databaseframe,image = RecImg)
    image.pack()

    capturedImgLabel = Label(matching_screen,text= percentage[0]+"% Match in "+"DataBase")
    capturedImgLabel.grid(row=6,column=6,rowspan=3)



    #Instructions 
    instLabel = Label(matching_screen,text =" Please wait matching in Database ",anchor=CENTER)
    instLabel.config(font=("Courier", 15))
    instLabel.grid(row=9,column=0,columnspan=8)

    print("Started the timer")
    matching_screen.after(2000,matching_screen.destroy)
    print("Destroyed")

###########################################################################################

def fin_screen():

    final_screen = Toplevel()
    final_screen.title("final_screen")
    final_screen.geometry("800x480+0+0")
    final_screen.overrideredirect(False) #Set this to true to disable minimize/exit bar


    #Blank Blocks : Only for astherics
    blank1 =Label(final_screen,text=" ",pady=28)
    blank1.grid(row =1,column =0,columnspan=8) #Blank Row below Org name

    blank2 =Label(final_screen,text=" ",pady=28)
    blank2.grid(row =5,column =0,columnspan=8) #Blank Row below photo and data dialogs

    blank3 =Label(final_screen,text="",padx=15)
    blank3.grid(row =1,column =0,rowspan=5) #Blank Column on left

    blank4 =Label(final_screen,text="",padx=15)
    blank4.grid(row =1,column =3,rowspan=5) #Blank Column in mid

    blank5 =Label(final_screen,text="",padx=15)
    blank5.grid(row =1,column =7,rowspan=5) #Blank Column on right




    #AT Bottom
    status= Label(final_screen,text="Developed In Delhi Technological University",bd = 1 ,relief=SUNKEN,anchor=E)
    status.grid(row=6,column =0 ,columnspan=8,sticky=W+E)



    #Organization Name Placement
    orgnameframe= LabelFrame(final_screen,padx=95,pady=15)
    orgnameframe.grid(row=0,column=0,columnspan=8)

    org_name = Label(orgnameframe,text = "Delhi Technological University",anchor=CENTER)  
    org_name.config(font=("Courier", 25))
    org_name.pack()


    #Photo Placement
    photoframe = LabelFrame(final_screen,padx=15,pady=12)
    photoframe.grid(row=2,column=1,rowspan=3,columnspan=2)

    if float(percentage[0]) >= threshold:
        image =Label(photoframe,image = RecImg)
        image.pack()
    else :
        image =Label(photoframe,image = CapImg)
        image.pack()



    #Welcome + Name
    
    if float(percentage[0]) >= threshold:
        name_to_print = str(names[0])
    else :
        name_to_print = "Anonymous"


    welcomeframe = LabelFrame(final_screen,padx=30,pady=25)
    welcomeframe.grid(row=2,column=4,columnspan=3)

    nameLabel = Label(welcomeframe,text = "Welcome "+ name_to_print ,anchor = W)
    nameLabel.pack() 



    #Attendence Status
    #status= " Succesfull"
    status = attendence
    attendenceframe = LabelFrame(final_screen,padx=30,pady=25)
    attendenceframe.grid(row=3,column=4,columnspan=3,sticky =W)

    attendenceLabel = Label(attendenceframe,text = "Attendence Status :"+ status ,anchor =W)
    attendenceLabel.pack() 



    final_screen.after(3000,final_screen.destroy)
    print("Destroyed final_screen")



###########################################################################################
def pop_matching_screen():
    mat_screen()

def pop_final_screen():
    fin_screen()

###########################################################################################



###########################################################################################
ideal_screen = Tk()
ideal_screen.title("ideal_screen")
ideal_screen.geometry("800x480+0+0")
ideal_screen.overrideredirect(False) #Set this to true to disable minimize/exit bar

RecievedDataFolder = '/home/jacksparrow/Desktop/Final_Fusion/Data Folder/Recieved Image/'
SentDataFolder = '/home/jacksparrow/Desktop/Final_Fusion/Data Folder/Sent Image/'

path_rec_img = "/home/jacksparrow/Desktop/Final_Fusion/Data Folder/Recieved Image/Resized1.jpg"
path_cap_img = "/home/jacksparrow/Desktop/Final_Fusion/Data Folder/Sent Image/TempImg.jpg"
path_logo ="/home/jacksparrow/Desktop/Final_Fusion/icon.jpg"

LogoImg = ImageTk.PhotoImage(Image.open("/home/jacksparrow/Desktop/icon.jpg"))




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

print("AT END OF FIRST SCREEN")

#######################################################################



Click_n_Crop_Fusion.CnC(5)
CapImg = ImageTk.PhotoImage(Image.open(path_cap_img))

names, percentage  =Communication_Fusion.Send_Img_Rec_Data(path_cap_img)

#Sending The Names And Getting the Attendence responce
threshold= 80.00 # Threshold on Percentage Match
attendence = Communication_Fusion.MarkingAttendence(names,percentage,threshold)
print("Attendence Status :", attendence)

matched_img = cv2.imread(RecievedDataFolder + 'Recieved1.jpg')

#print('Original Dimensions : ',matched_img.shape)
width = 120
height = 160
dim = (width, height)

# resize image
resized = cv2.resize(matched_img, dim, interpolation = cv2.INTER_AREA)

#print('Resized Dimensions : ',resized.shape)

cv2.imwrite(RecievedDataFolder+'Resized1.jpg',resized)
RecImg = ImageTk.PhotoImage(Image.open(path_rec_img))



ideal_screen.after(3000,pop_matching_screen)

ideal_screen.after(5000,pop_final_screen)


mainloop()

