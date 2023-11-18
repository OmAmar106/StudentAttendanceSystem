#ALL MODULES NOT DOWNLOADED AND SQL NOT AVAILABLE SO WON'T WORK
import pymysql as pym
import qrcode
import random
import string
import webbrowser
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import ast
mycon = pym.connect(host="localhost",user="root",password="",autocommit=True)
cursor = mycon.cursor()
cursor.execute("CREATE DATABASE if not exists AttSys ;")
cursor.execute("USE AttSys;")
cursor.execute("CREATE TABLE if not exists Messages(Subject VARCHAR(100),Messages VARCHAR(700),Class VARCHAR(3),Date date) ;")
a=random.randint(0,10)
b=random.randint(0,10)
print("Please solve this question (not a robot): ")
d = "+"
e = "="
c = int(input(str(a)+" "+d+" "+str(b)+" "+" "+e+" "))
e = a+b
if type(c)==int and e == c :
    print("Verified Successfully!")
    while True:
        print("\n")
        print ("------------------WELCOME TO SCHOOL MANAGEMENT SYSTEM------------------")
        print("\n1.Admin")
        print("2.Student")
        print("3.Teacher")
        print("4.Exit")
        role=int(input("\nEnter 1/2/3/4: "))
        if role == 1 :
            username = input("\nEnter username: ")
            password = input("Enter password: ")
            if username == "admin" and password == "#pas123":
                print("\nLogin succesful.")
                while True:
                    print("\n1.Create New ID")
                    print("2.View List")
                    print("3.Delete ID")
                    print("4.Dashboard")
                    print("5.Exit")
                    yn = input("Please enter 1/2/3/4/5: ")
                    if yn == "1" :
                        while True:
                            print("1.Create New Student")
                            print("2.Create New Teacher")
                            print("3.Back")
                            yn1 = input("Please enter 1/2/3: ")
                            if yn1 == "1":
                                cursor.execute("CREATE TABLE if not exists Students(UserName VARCHAR(20),Class VARCHAR(3),Age VARCHAR(2),Password VARCHAR(10));")
                                while True:
                                    yn1o1 = input("Enter Username : ")
                                    statement = "SELECT Username FROM Students WHERE UserName = '"+yn1o1+"';"
                                    cursor.execute(statement)
                                    rowsa = cursor.fetchall()
                                    if len(rowsa)==0:
                                        if (yn1o1.strip()).isalpha():
                                            while True:
                                                yn1o2 = input("Enter Class (XXX) : ")
                                                if yn1o2[-1:].isalpha():
                                                    if len(yn1o2)>3:
                                                        print("The value should be 3 or less")
                                                        continue
                                                    elif len(yn1o2)==3 and yn1o2[:2].isdigit():
                                                        if int(yn1o2[:2])>12:
                                                            print("Maximum class possible is 12")
                                                        else:
                                                            break
                                                    elif len(yn1o2)==3 and yn1o2[:2].isdigit() == False :
                                                        print("First 2 characters should be digits of class")
                                                    else:
                                                        break
                                                else:
                                                    print("The last character should be division")
                                                    continue
                                            yn1o2 = yn1o2[:2]+yn1o2[-1:].upper()
                                            while True:
                                                yn1o3 = int(input("Enter Age : "))        
                                                if yn1o3 > 20 or yn1o3 < 6:
                                                    print("Please enter correct Age.")
                                                    continue
                                                else:
                                                    break
                                            while True:
                                                yn1o4 = str(input("Enter password(Enter Random for Random Password) : "))#atleast one integer and 6 digits
                                                if yn1o4 == "Random" or yn1o4 == "random":
                                                    number1 = random.randint(100,1000)
                                                    number1list = list(str(number1))
                                                    extra = ["@","#"]
                                                    alphabet1 = random.sample(string.ascii_lowercase,3)
                                                    List = number1list + alphabet1
                                                    random.shuffle(List)
                                                    List = "".join(List)
                                                    yn1o4 = List
                                                    break
                                                else:
                                                    for i in yn1o4:
                                                        if i.isnumeric():
                                                            yn1o4o1 = True
                                                            break
                                                        else:
                                                            yn1o4o1 = False
                                                            continue
                                                    if len(yn1o4)<5 or yn1o4o1 == False:
                                                        print("Please enter more than 5 characters or enter atleast one integer")
                                                        continue
                                                    else:
                                                        break
                                            print("Your password is :",yn1o4)
                                            sentence = "INSERT INTO Students VALUES('"+yn1o1+"','"+str(yn1o2)+"','"+str(yn1o3)+"','"+str(yn1o4)+"');"
                                            cursor.execute(sentence)
                                            break
                                        else:
                                            print("Please enter string / only first name")
                                            continue
                                    else:
                                        print("Username already taken. Kindly take something else")
                                        continue
                            elif yn1 == "2":
                                cursor.execute("CREATE TABLE if not exists Teachers(UserName VARCHAR(20),Subject VARCHAR(20),Age VARCHAR(2),Password VARCHAR(20));")
                                while True:
                                    yn2o1 = input("Enter Username : ")
                                    statement2 = "SELECT Username FROM Teachers where UserName = '"+yn2o1+"';"
                                    cursor.execute(statement2)
                                    rowsb = cursor.fetchall()
                                    if len(rowsb)==0:
                                        if (yn2o1.strip()).isalpha():
                                            while True:
                                                yn2o2 = input("Enter Subject(P/C/M/B/CS/E) : ")
                                                if yn2o2 == "P":
                                                    yn2o2 = "Physics"
                                                    break 
                                                elif yn2o2 == "C":
                                                    yn2o2 = "Chemistry"
                                                    break
                                                elif yn2o2 == "M":
                                                    yn2o2 = "Maths"
                                                    break
                                                elif yn2o2 == "B":
                                                    yn2o2 = "Biology"
                                                    break
                                                elif yn2o2 == "CS":
                                                    yn2o2 = "Computer"
                                                    break
                                                elif yn2o2 == "E":
                                                    yn2o2 = "English"
                                                    break
                                                else:
                                                    print("Please enter P/C/M/B/CS/E or enter in uppercase")
                                                    continue
                                            while True:
                                                yn2o3 = int(input("Enter Age : "))        
                                                if yn2o3 > 80 :
                                                    print("Please enter correct Age.")
                                                    continue
                                                else:
                                                    break
                                            while True:
                                                yn2o4 = str(input("Enter password(Enter Random for Random Password) : "))#atleast one integer and 6 digits
                                                if yn2o4 == "Random" or yn2o4 == "random":
                                                    number2 = random.randint(100,1000)
                                                    number2list = list(str(number2))
                                                    extra = ["@","#"]
                                                    alphabet2 = random.sample(string.ascii_lowercase,3)
                                                    List = number2list + alphabet2
                                                    random.shuffle(List)
                                                    List = "".join(List)
                                                    yn2o4 = List
                                                    break
                                                else:
                                                    for i in yn2o4:
                                                        if i.isnumeric():
                                                            yn2o4o1 = True
                                                            break
                                                        else:
                                                            yn2o4o1 = False
                                                            continue
                                                    if len(yn2o4)<5 or yn2o4o1 == False:
                                                        print("Please enter more than 5 characters or enter atleast one integer")
                                                        continue
                                                    else:
                                                        break
                                            print("Your password is :",yn2o4)
                                            sentence2 = "INSERT INTO Teachers VALUES('"+yn2o1+"','"+str(yn2o2)+"','"+str(yn2o3)+"','"+str(yn2o4)+"');"
                                            cursor.execute(sentence2)
                                            break
                                        else:
                                            print("Please enter string / only first name")
                                            continue
                                    else:
                                        print("Username already taken. Kindly take something else")
                                        continue 
                            elif yn1 == "3":
                                break
                            else :
                                print("Please enter 1 or 2 or 3")
                                continue
                    elif yn == "2" :
                        print("1.Student List")
                        print("2.Teacher List")
                        print("3.Message List")
                        print("4.Back")
                        while True:
                            yn2 = input("Please enter 1/2/3/4 : ")
                            if yn2 == "1":
                                yn2o1 = int(input("Enter Class(1-12) : "))
                                if yn2o1 < 13 and yn2o1 > 0 :
                                    yn2o1o1= input("Enter Section: ")
                                    if yn2o1o1.isalpha() and len(yn2o1o1)==1:
                                        yn2o1o1 = str(yn2o1) + yn2o1o1.upper()
                                        sentence3 = "SELECT UserName,Class,Age FROM Students WHERE Class = '"+yn2o1o1+"' ORDER BY UserName;"
                                        cursor.execute(sentence3)
                                        data1 = cursor.fetchall()
                                        for row in data1:
                                            print(row)
                                    else:
                                        print("Please enter a valid alphabet")
                                        continue
                                else:
                                    print("Class doesn't exist!")
                                    continue
                            elif yn2 == "2":
                                sentence4 = "select UserName,Subject,Age from Teachers ORDER BY UserName;"
                                cursor.execute(sentence4)
                                data2 = cursor.fetchall()
                                for row in data2:
                                    print(row)
                            elif yn2 == "3":
                                cursor.execute("SELECT * FROM Messages")
                                data3 = cursor.fetchall()
                                for row in data3:
                                    print(row)
                            elif yn2 == "4":
                                break
                    elif yn == "3" :#delete id
                        while True:
                            print("1.Delete Student")
                            print("2.Delete Teacher")
                            print("3.Back")
                            yn3 = input("Enter 1/2/3 : ")
                            if yn3 == "1":
                                namedel = input("Enter name to be deleted : ")
                                sent = "DELETE FROM Students WHERE UserName = '"+namedel+"';"
                                cursor.execute(sent)
                                print("DELETED SUCCESSFULLY!")
                            elif yn3 == "2":
                                namedel1 = input("Enter name to be deleted : ")
                                sent1 = "DELETE FROM Teachers WHERE UserName = '"+namedel1+"';"
                                cursor.execute(sent1)
                                print("DELETED SUCCESSFULLY!")
                            else:
                                break
                    elif yn == "4" :
                        break
                    elif yn == "5" :
                        exit()
        elif role == 2 :
            c=1
            while c==1:
                usernamea = input("Enter Username : ")
                passworda = input("Enter Password : ")
                L = (usernamea,passworda,)
                sentence3 = "SELECT UserName,Password FROM Students ;"
                cursor.execute(sentence3)
                data3 = cursor.fetchall()
                for row in data3:
                    if L==row:
                        print("Login Successful!")
                        while True:
                            print("\n1.Qr Code Scanner")
                            print("2.Messages")
                            print("3.Change password")
                            print("4.Dashboard")
                            print("5.Exit")
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
                                sentence4 = "SELECT Class FROM Students WHERE UserName = '"+usernamea+"' ;"
                                cursor.execute(sentence4)
                                data4 = cursor.fetchone()
                                sentence5 = "SELECT Subject FROM Messages WHERE Class = '"+data4[0]+"';"
                                cursor.execute(sentence5)
                                data5 = cursor.fetchall()
                                n = 1
                                L2 = []
                                for row in data5 :
                                    L2.append(row)
                                    print(n,".",row)
                                    n = n+1
                                ask = int(input("Enter the number of messages you want to view : "))
                                if ask > (n-1) and ask!=0:
                                    print("SORRY you're over the number limit!")
                                    continue
                                elif ask == 0 :
                                        print("ERROR!")
                                else:
                                    ask = ask-1
                                    gh = L2[ask]
                                    sent3 = "SELECT Messages FROM Messages WHERE subject = '"+gh[0]+"';"
                                    cursor.execute(sent3)
                                    data6 = cursor.fetchall()
                                    for row in data6 :
                                        print(row)
                                    o = input("Press ENTER to continue:")
                                    break
                            elif role1 == 3 :
                                print("You can only change the password once every login")
                                oldpas = input("Enter Old Password : ")
                                if oldpas == passworda :
                                    newpas = input("Enter New Password : ")
                                    if len(newpas)>5:
                                        sent7 = "UPDATE Students SET Password = '"+newpas+"' where UserName = '"+usernamea+"';"
                                        cursor.execute(sent7)
                                    else:
                                        print("Your password is too short!")
                                        break
                                    break
                            elif role1 == 4:
                                c=2
                                break
                            else:
                                exit()
                else:
                    print("....")
                    c = 5
                    continue
            
        elif role == 3 :
                    while True:
                        usernameb = input("Enter Username : ")
                        passwordb = input("Enter Password : ")
                        L = (usernameb,passwordb,)
                        sentence10 = "SELECT UserName,Password from Teachers;"
                        cursor.execute(sentence10)
                        data10 = cursor.fetchall()
                        for row in data10:
                            if L==row:
                                print("\n1.Qr Code Generator")
                                print("2.Student List")
                                print("3.Send message to students:")                     
                                print("4.Change password")
                                print("5.Dashboard")
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
                                    yn3o1 = int(input("Enter Class(1-12) : "))
                                    if yn3o1 < 13 and yn3o1 > 0 :
                                        yn3o1o1= input("Enter Section: ")
                                        if yn3o1o1.isalpha() and len(yn3o1o1)==1:
                                            yn3o1o1 = str(yn3o1) + yn3o1o1.upper()
                                            sentence8 = "SELECT UserName,Class,Age from Students where Class = '"+yn3o1o1+"' ORDER BY UserName;"
                                            cursor.execute(sentence8)
                                            data1 = cursor.fetchall()
                                            for row in data1:
                                                print(row)
                                            o = input("Press any key to continue")
                                        else:
                                            print("Please enter a valid alphabet")
                                            continue
                                    else:
                                        print("Class doesn't exist!")
                                        continue
                                elif role2 == 3 :
                                    subjecta = input("Enter Subject(Topic) : ")
                                    messagea = input("Enter Message : ")
                                    while True:
                                        ynx = input("Enter Class (XXX) : ")
                                        if ynx[-1:].isalpha():
                                            if len(ynx)>3:
                                                print("The value should be 3 or less")
                                                continue
                                            elif len(ynx)==3 and ynx[:2].isdigit():
                                                if int(ynx[:2])>12:
                                                    print("Maximum class possible is 12")
                                                else:
                                                    break
                                            elif len(ynx)==3 and ynx[:2].isdigit() == False :
                                                print("First 2 digits should be class!")
                                            else:
                                                break
                                        else:
                                            print("The last digit should be class!")
                                            continue
                                    ynx = ynx[:2]+ynx[-1:].upper()
                                    statement11 = "INSERT INTO Messages VALUES('"+subjecta+"','"+messagea+"','"+ynx+"',curdate());"
                                    cursor.execute(statement11)
                                elif role2 == 4 :
                                    print("You can only change the password once every login")
                                    oldpasb = input("Enter Old Password : ")
                                    if oldpasb == passwordb :
                                        newpasb = input("Enter New Password : ")
                                        if len(newpasb)>5:
                                            sent9 = "UPDATE Teachers SET Password = '"+newpasb+"' where UserName = '"+usernameb+"';"
                                            cursor.execute(sent9)
                                        else:
                                            print("Your password is too short!")
                                            break
                                        break
                                elif role2 == 5 :
                                    break
                                elif role2 == 6 :
                                    exit()
                                else:
                                    print("Please enter from 1 to 5:")
                        else:
                            print(".....")
                            break
        elif role == 4:
            exit()
            mycon.close()
        else :
            print("\nPlease enter 1/2/3/4.")
            b = input("Press Enter to go to Main Menu")
else:
    print("Unsuccessful! You weren't able to solve the question correctly.")
mycon.close()
