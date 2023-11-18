import qrcode
import random
import webbrowser
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import ast
a=random.randint(0,10)
b=random.randint(0,10)
c = "a + b"
print("Solve this question (not a robot) : ")
d = "+"
e = "="
c = int(input(str(a)+" "+d+" "+str(b)+" "+" "+e+" "))
e = a+b
if e == c :
    print("Verified Successfully!")
    while True:
        print("\n")
        print ("------------------Welcome to School Management System------------------")
        print("\n1.Admin")
        print("2.Student")
        print("3.Teacher")
        print("4.exit")
        role=int(input("\nEnter 1/2/3/4: "))
        if role == 1 :
            username = input("\nEnter username: ")
            password = input("Enter password: ")
            if username == "admin" and password == "#pas123":
                print("\nLogin succesful.")
                while True:
                    print("\n1.Student New ID")
                    print("2.Teacher New ID")
                    print("3.Teacher List")
                    print("4.Dashboard")
                    print("5.Delete Student")
                    print("6.Delete Teacher")
                    print("7.exit")
                    yn = input("Enter 1/2/3/4/5/6/7: ")
                    if yn == "1" :
                        text_file = open("Usernamecreator.txt", "a+")
                        text_fileread = open("Usernamecreator.txt", "r")
                        text_filea = open("passwordcreator.txt", "a+")
                        content = text_fileread.readlines()
                        z = len(content)
                        for i in range(50):
                            create_username = input("Enter username: ")
                            for i in range (z):
                                if create_username == content[i].strip():
                                    print("Username already taken!")
                                    break
                            else:
                                text_file.write("{}\n".format(create_username))
                                create_password = input("Enter password: ")
                                text_filea.write("{}\n".format(create_password))
                                ask1 = input("Do u want to continue?(Yes/No): ")
                                if ask1 == "No" or ask1 == "no":
                                    text_file.close()
                                    text_filea.close()
                                    break                                               
                    elif yn == "2" :
                        text_fileb = open("Usernamecreatorteach.txt","a+")
                        text_filebread = open("Usernamecreatorteach.txt","r")
                        text_filec = open("passwordcreatorteach.txt","a+")
                        content = text_filebread.readlines()
                        z = len(content)
                        for i in range(20):
                            create_usernamea = input("Enter username: ")
                            for i in range(z):
                                if create_usernamea == content[i].strip():
                                    print("Username already taken!")
                                    break                            
                            else:
                                text_fileb.write("{}\n".format(create_usernamea))
                                create_passworda = input("Enter password: ")
                                text_filec.write("{}\n".format(create_passworda))
                                ask1 = input("Do u want to continue? (Yes/No):")
                                if ask1 == "No" or ask1 == "no":
                                    text_fileb.close()
                                    text_filec.close()
                                    break                         
                    elif yn == "3" :
                        text_filea1 = open("Usernamecreatorteach.txt","r")
                        content = text_filea1.readlines()
                        z = len(content)
                        for i in range(z):
                            print(i+1,".",content[i].strip())
                        y = input("Press Enter to go to the Main Menu: ")
                    elif yn == "4" :
                        break
                    elif yn == "5" :
                        text_file = open("Usernamecreator.txt", "r")                        
                        text_filea = open("passwordcreator.txt", "r")                       
                        content = text_file.readlines()
                        content1 = text_filea.readlines()                        
                        a = input("Enter the Student name to be deleted:")                        
                        for line in content:
                            b = 0                           
                            if a in line:                                                                
                                for line in content:
                                    if line.strip() == a:
                                        break
                                else:
                                    b += 1                                        
                                text_filewrite = open("Usernamecreator.txt", "w")
                                for line in content:
                                    if line.strip() != a:
                                        text_filewrite.write(line)                                     
                                text_filewrite.close()
                                del content1[b]
                                text_fileawrite = open("passwordcreator.txt","w")
                                for line in content1:
                                    text_fileawrite.write(line)
                                text_fileawrite.close()
                                print("Student name deleted succesfully. ")
                                text_file.close()
                                text_filea.close()
                                z23= input("Press Enter to go to the Main Menu:")
                                break
                        else:
                            print("Student doesn't exist!")
                            k = input("Press Enter to go to the Main Menu:")                                                          
                    elif yn == "6" :
                        text_filec = open("Usernamecreatorteach.txt", "r")                        
                        text_filed = open("passwordcreatorteach.txt", "r")                    
                        content2 = text_filec.readlines()
                        content3 = text_filed.readlines()                        
                        er = input("Enter the Teacher name to be deleted:")
                        for line in content2:
                            b = 0 
                            if er in line :
                                for line in content2:                                    
                                    if line.strip() == er:                                
                                        break
                                else:
                                    b += 1                                        
                                text_filecwrite = open("Usernamecreatorteach.txt", "w")
                                for line in content2:
                                    if line.strip() != er:
                                        text_filecwrite.write(line)
                                text_filecwrite.close()
                                del content3[b]
                                text_filedwrite = open("passwordcreatorteach.txt","w")
                                for line in content3:
                                    text_filedwrite.write(line)
                                text_filedwrite.close()
                                print("Teacher name deleted succesfully. ")
                                text_filec.close()
                                text_filed.close()
                                z23= input("Press Enter to go to the Main Menu:")
                                break
                        else:
                            print("Teacher doesn't exist!")
                            l = input("Press Enter to go to the Main Menu:")                                             
                    elif yn == "7" :
                        exit()
                    else:
                        print("\nEnter a number from 1/2/3/4/5 ")
            else:
                print("Incorrect Username or Password.Please try again!")
        elif role == 2 :
            username = input("\nEnter name: ")
            password = input("Enter password: ")
            text_file = open("Usernamecreator.txt", "r+")
            text_filea = open("passwordcreator.txt", "r+")
            content = text_file.readlines()
            content1 = text_filea.readlines()
            z = len(content)
            for i in range (z):
                if username == content[i].strip() and password == content1[i].strip():
                    print("Login successful.")
                    while True:
                        print("1.Qr Code Scanner")
                        print("2.Change password")
                        print("3.Messages")
                        print("4.Dashboard")
                        print("5.Change password")
                        print("6.Exit")
                        role1 = int(input("\nEnter 1/2/3/4/5/6 : "))
                        if role1 == 1 :
                            print("\nQr Code Scanner:")
                            links = []
                            def decoder(image):
                                gray_img = cv2.cvtColor(image,0)
                                barcode = decode(gray_img)
                                for obj in barcode:
                                    points = obj.polygon
                                    (x,y,w,h) = obj.rect
                                    pts = np.array(points, np.int32)
                                    pts = pts.reshape((-1, 1, 2))
                                    cv2.polylines(image, [pts], True, (0, 255, 0), 3)
                                    barcodeData = obj.data.decode("utf-8")
                                    barcodeType = obj.type
                                    string = "Data: " + str(barcodeData) + " | Type: " + str(barcodeType)
                                    link = str(barcodeData)
                                    if link not in links:        
                                        links.append(link)
                                        cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255), 2)
                                        print("Barcode: "+barcodeData +" | Type: "+barcodeType)
                                        webbrowser.open(link)
                            cap = cv2.VideoCapture(0)
                            while True:
                                ret, frame = cap.read()
                                decoder(frame)
                                cv2.imshow('Image', frame)
                                code = cv2.waitKey(10)
                                if code == ord('q'):
                                    break                           
                        elif role1 == 2 :
                            es = input("Enter old password: ")
                            if es == content1[i].strip():                               
                                ed = input("Enter new password: ")
                                content1[i] = ed
                            else :
                                print("Sorry wrong password.")
                        elif role1 == 3 :
                            text_filezread = open("name.txt","r")
                            text_fileyread = open("message.txt","r")
                            content1 = text_fileyread.readlines()
                            content = text_filezread.readlines()
                            df = len(content1)
                            dg = len(content)
                            print("To view messages, enter a number from 1 to",dg)
                            dl = int(input("Enter the number: "))
                            if dl <= dg and dl >= 1 :
                                dl = dl-1
                                print("by - ",content[dl])
                                print(content1[dl])
                                n = input("Press Enter to continue!")
                            else:
                                print("Please don't enter a number which is not in the values!")
                        elif role1 == 4 :
                            break
                        elif role1 == 5:
                            text_filez = open("passwordcreator.txt","r")
                            content = text_filez.readlines()
                            passw=input("Enter old password : ")
                            if passw == password :
                                b = input("enter new password : ")
                                content[i]=b+"\n"
                                text_filez = open("passwordcreator.txt","w")
                                text_filez.writelines(content)
                                text_filez.close()
                                print("Password changed successfully!")
                                a = input("Press Enter to go to menu!")
                            else:
                                print("Wrong Password!")
                                b = input("Press Enter to go to menu!")
                        elif role1 == 6 :
                            exit()
                        else:
                            print("Enter a number from 1 to 5:")                
            else:
                print("Incorrect Username or Password.Please try again!")
            text_file.close()
            text_filea.close()
        elif role == 3 :
            username = input("\nEnter name: ")
            password = input("Enter password: ")
            text_file = open("Usernamecreator.txt", "r+")
            text_fileb = open("Usernamecreatorteach.txt", "r+")
            text_filec = open("passwordcreatorteach.txt", "r+")
            content4 = text_file.readlines()
            content2 = text_fileb.readlines()
            content3 = text_filec.readlines()
            x = len(content2)
            y = len(content4)
            for i in range (x):
                if username == content2[i].strip() and password == content3[i].strip():
                    print("\nLogin successful.")
                    while True:
                        print("\n1.Qr Code Generator")
                        print("2.Student List")
                        print("3.Send message to students:")
                        print("4.Dashboard")
                        print("5.Change password")
                        print("6.Exit")
                        role2 = int(input("Enter 1/2/3/4/5/6 : "))
                        if role2 == 1 :
                            print("Qr Code Generator:")
                            qr = qrcode.QRCode(version=1,box_size=15,border=5)
                            link = input("Enter the link:")
                            data = link
                            qr.add_data(data)
                            qr.make(fit=True)
                            img = qr.make_image(fill='black',back_color='white')
                            img.save('Attendance_QRCode.png')
                            img = input("You will be able to find the image in the same directory as this file.")
                        elif role2 == 2 :
                            print("Student List:")
                            for j in range(y):
                                print(content4[j])
                            img1 = input("Press Enter to go to Main Menu:")
                        elif role2== 3:
                            text_filez = open("name.txt","a+")
                            text_filey = open("message.txt","a+")
                            content1 = text_filey.readlines()
                            content = text_filez.readlines()
                            message=input("Message:")
                            text_filez.write("{}\n".format(username))
                            text_filey.write("{}\n".format(message))
                            print("Message sent successfully!")
                            text_filez.close()
                            text_filey.close()
                        elif role2 == 4 :
                            break
                        elif role2 == 5 :
                            text_filez = open("passwordcreatorteach.txt","r")
                            content = text_filez.readlines()
                            passw=input("Enter old password : ")
                            if passw == password :
                                b = input("Enter new password : ")
                                content[i]=b+"\n"
                                text_filez = open("passwordcreatorteach.txt","w")
                                text_filez.writelines(content)
                                text_filez.close()
                                print("Password changed successfully!")
                                a = input("Press enter to go to Menu:")
                            else:
                                print("Wrong password!")
                                b = input("Press enter to go to Menu:")
                        elif role2 == 6 :
                            exit()
                        else:
                            print("Please enter from 1 to 5:")
            else:
                print("Incorrect Username or Password.Please try again!")
        elif role == 4:
            exit()
        else :
            print("\nEnter 1/2/3/4.")
else:
    print("Unsuccessful! , you weren't able to solve the question correctly! ")
