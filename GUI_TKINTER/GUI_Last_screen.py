import tkinter
from tkinter import *
import PIL
from PIL import Image, ImageTk



final_screen = Tk()
final_screen.title("final_screen")
final_screen.geometry("800x480+0+0")
final_screen.overrideredirect(False) #Set this to true to disable minimize/exit bar

gridtest = Tk()
gridtest.title("GRID TEST WINDOW")
gridtest.geometry("800x480+0+0")




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

RecImg = ImageTk.PhotoImage(Image.open('/home/jacksparrow/Desktop/Final_Fusion/Data Folder/Sent Image/' + "TempImg.jpg"))

image =Label(photoframe,image = RecImg)
image.pack()



#Welcome + Name
name = "Harsh Kaushal"

welcomeframe = LabelFrame(final_screen,padx=30,pady=25)
welcomeframe.grid(row=2,column=4,columnspan=3)

nameLabel = Label(welcomeframe,text = "Welcome "+name ,anchor = W)
nameLabel.pack() 



#Attendence Status
status= " Succesfull"

attendenceframe = LabelFrame(final_screen,padx=30,pady=25)
attendenceframe.grid(row=3,column=4,columnspan=3,sticky =W)

attendenceLabel = Label(attendenceframe,text = "Attendence Status :"+ status ,anchor =W)
attendenceLabel.pack() 





#Grid test window
for i in [0,1,2,3,4,5]:
    for j in [0,1,2,3,4,5,6,7]:
        gridframe = LabelFrame(gridtest,padx=30,pady=25)
        gridframe.grid(row=i,column=j)
        staticLabel = Label(gridframe,text = str(i) +" x " + str(j) ) 
        staticLabel.pack() 







final_screen.mainloop()