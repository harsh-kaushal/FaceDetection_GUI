import os
import requests
import base64
import io

from cv2 import cv2
import numpy as np

import urllib3
urllib3.disable_warnings()

RecievedDataFolder = '/home/jacksparrow/Desktop/Final_Fusion/Data Folder/Recieved Image/' 

def Send_Img_Rec_Data(path):
    
    print("####### Send_Img_Rec_Data ########")
    
    with open(path, "rb") as img:
	    my_img_string = base64.b64encode(img.read())

    url1 = 'https://www.ai.dtu.ac.in/something'
    files1 ={
        "dataset" : 'jush222', 
        "imageString" : my_img_string,
        }
    payload1 ={
        "Content-Type" :'application/json'#;charset=UTF-8'
        }
        
    with requests.Session() as s1:
        r1 = s1.post(url1,json=files1,params=payload1)
        recieved1 = r1.json()

    #print("************")
    #print(r1.text)
    #print("************")

    if (r1.status_code != 200):
        print(r1.status_code)
        return("SERVER DOWN")
        #Server Down Window
        #Jump TO starting
        print("####### ------------- ########")



    else :

        #Saving The images Recieved
        RecievedFilenames = ['Recieved1.jpg','Recieved2.jpg','Recieved3.jpg']
        imgRec=[""]*3
        for j in [0,1,2]:
            imgRec[j] = recieved1['imageString'][j]
            imgRec[j] = base64.b64decode(imgRec[j])
            with open(RecievedDataFolder + RecievedFilenames[j], 'wb') as f:
                f.write(imgRec[j])


        #Printing the Percentage Match of best three
        percentageMatch = [""]*3
        for i in [0,1,2]:
            percentageMatch[i] = os.path.basename(recieved1['percentage'][i])
            percentageMatch[i] = percentageMatch[i].replace('%','') # TO remove % sign from 

        print(percentageMatch[0])
        print(percentageMatch[1])
        print(percentageMatch[2])
        print("---------------")


        #Printing the names recieved after sending photo
        namesRec=[""]*3
        temp =["",""]*3
        for i in [0,1,2]:
            without_extra_slash = os.path.normpath(recieved1['name'][i])
            namesRec[i] = os.path.basename(os.path.splitext(without_extra_slash)[0])

        print(namesRec[0])
        print(namesRec[1])
        print(namesRec[2])
        print("---------------")

        print("####### ------------- ########")
        return(namesRec,percentageMatch)



def MarkingAttendence(namesRec,percentageMatch,threshold):
    
    print("####### MarkingAttendence ########")

    if float(percentageMatch[0]) >= threshold:
        name = namesRec[0]
        print(name)
    else :
        name =" "

    url2 = 'https://www.ai.dtu.ac.in/api/databases/attendance'
    files2 ={
        "database" : 'jush222', 
        "attendance" :name,
        }
    payload2 ={
        "Content-Type" :'application/json'#;charset=UTF-8'
        }
        
    with requests.Session() as s2:
        r2 = s2.post(url2,json=files2,params=payload2)
        recieved2 = r2.json()

    #print(r2.text)
    attendence_status = recieved2['result']
    print(attendence_status)


    if attendence_status == 'done':
        print("Marked Succesfully")
        print("####### ------------- ########")
        return('Present')

    if attendence_status == 'attribute error':
        print("Sorry Cant Recognize")
        print("####### ------------- ########")
        return('Failed')


