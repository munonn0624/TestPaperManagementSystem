#Module/Program name:P1G1course.py
#date created       :17th March 2023
#created by         :Lee Wei Jin
#import             :os(system clear screen),json
#modification       :no repeated input(course code and course name),
#                    arrange course code added or updated according alphabet,
#                    skip if do not wish to update course code or course name,
#                    clear screen after every input

import os, json

def displayLst(lst):
    print("-"*65)
    print("Courses Maintenance")
    print("-"*65)
    if len(lst)==0:
        print("No records available")
    else:
        print("Num Code      Description")
        print("-"*65)
        for i in range(len(lst)):   
            print("%2d  %s  %s"%((i+1),lst[i][0],lst[i][1]))
    print("-"*65)
        
def delUpd(lst,opt):
    optLst =["U","D"]
    optDLst=["Modify","Delete"]
    cont="C"
    step=1
    while cont=="C":
        if step==1:
            idx=optLst.index(opt)
            os.system("cls")
            displayLst(lst)
            recID=input("Rec to          Stop <Q>uit >> ").upper()
            if recID=="Q":
                step=99
            elif not recID.isdigit(): 
                print("Invalid record number entered. Press enter to continue")
                input()
                os.system("cls")
                displayLst(lst)
            else:
                recID=int(recID)
                num=[x[0] for x in lst]
                if recID > len(num):
                    print("Not enough course. Press enter to continue")
                    input()
                elif recID==0:
                    print("Wrong data. Press enter to continue")
                    input()
                else:
                    code  =lst[recID-1][0]
                    course=lst[recID-1][1]
                    step +=1
        if step==2:
            os.system("cls")
            displayLst(lst)
            if opt=="D": 
                print("Enter course code <Q>uit >> %s"%code)
                print("Enter course name <Q>uit >> %s"%course)
                step=4
            else:
                print("Press <S> if do not wish to change this data")
                print("Record number >> %d"%recID)
                ncode=input("Please enter course code <S>kip <Q>uit >> ").upper()
                clst=[x[0] for x in lst]
                if ncode=="Q":
                    step=99
                elif ncode=="S":
                    ncode=code
                    step +=1
                elif ncode[4:8].isdigit() and ncode[:4].isalpha():
                    if len(ncode)!=8:
                        print("Data entered must have 4 alphabets before 4 digits. Press enter to continue")
                        input()
                    elif ncode in clst:
                        print("Course code repeated. Press enter to continue")
                        input()
                    else:
                        step+=1
                else:
                    print("Data entered must have 4 alphabets before 4 digits. Press enter to continue")
                    input()
                
        if step==3:
            os.system("cls")
            displayLst(lst)
            print("Press <S> if do not wish to change this data")
            print("Record number >> %d"%recID)
            print("Please enter course code <S>kip <Q>uit >> %s"%ncode)
            validCharacters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
            ncourse = input("Enter course name Stop <S>kip <Q>uit >> ").upper()
            nlst=[x[1] for x in lst]
            if ncourse=="Q":
                step=99
            elif ncourse=="S":
                ncourse=course
                step +=1
            elif ncourse=="":
                print("Error with data entered.Please enter data without any digit or punctuation mark. Press enter to continue.")
                input()
                print("Record number >> %d"%recID)
                print("Enter course code <S>kip <Q>uit >> %s"%ncode)
            elif all(char in validCharacters for char in ncourse):
                if ncourse in nlst:
                    print("Course name repeated. Press enter to continue")
                    input()
                else:
                    step+=1
            else:
                print("Error with data entered.Please enter data without any digit or punctuation mark. Press enter to continue.")
                input()
                print("Record number >> %d"%recID)
                print("Enter course code <S>kip <Q>uit >> %s"%ncode)
                
        if step==4:
            if opt=="D":
                lst.pop(recID-1)
                print("Record deleted. Press enter to continue")
                input()
            else:
                os.system("cls")
                displayLst(lst)
                print("Record number >> %d"%recID)
                print("Course Code <Q>uit >> %s"%ncode)
                print("Course name <Q>uit >> %s"%ncourse)
                recID=int(recID)
                lst[recID-1]=[ncode, ncourse]
                print("Record updated. Press enter to continue")
                input()
            step=1
            
        if step==99:
            os.system("cls")
            cont="Q"
    return lst      
        
def addcourse(lst):
    cont="C"
    step=1
    while cont=="C":
        if step==1:
            os.system("cls")
            displayLst(lst)
            code=input("Enter course code added <Q>uit >>").upper()
            clst=[x[0] for x in lst]
            if code=="Q":
                step=99
            else:
                if code[4:8].isdigit() and code[:4].isalpha():
                    if code in clst:
                        print("Course code repeated.Press enter to continue.")
                        input()
                    elif len(code)!=8:
                        print("Data entered must have 4 alphabets before 4 digits. Press enter to continue")
                        input()
                    else:
                        step+=1
                else:
                    print("Data entered must have 4 alphabets before 4 digits. Press enter to continue")
                    input()
        if step==2:
            os.system("cls")
            displayLst(lst)
            print("Enter the course code <Q>uit >> %s"%code)
            validCharacters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
            course = input("Enter course name <Q>uit >> ").upper()
            nlst=[x[1] for x in lst]
            if course=="":
                print("Error with data entered.Please enter data without any digit or punctuation mark. Press enter to continue")
                input("")
                os.system("cls")
                displayLst(lst)
                print("Enter course code added <Q>uit >> %s"%code)
            elif course=="Q":
                step=99
            elif all(char in validCharacters for char in course):
                if course in nlst:
                        print("Course name repeated. Press enter to continue")
                        input()
                else:
                    step+=1
            else:
                print("Error with data entered.Please enter data without any digit or punctuation mark. Press enter to continue.")
                input("")
        if step==3:
            os.system("cls")
            displayLst(lst)
            print("Course Code <Q>uit >> %s"%code)
            print("Course name <Q>uit >> %s"%course)
            print("Record added. Press enter to continue")
            input()
            lst.append([code, course])
            f=open("courses.txt","a")
            f.write(str(lst.append))
            f.close()
            os.system("cls")
            return lst
        
        if step==99:
            os.system("cls")
            cont="Q"
    return lst
        
def readFile():
    import json
    f=open("courses.txt","r")
    lst=json.load(f)
    lst.sort()
    f.close()
    return lst

def saveFile(recLst):
    import json
    f=open("courses.txt","w")
    json.dump(recLst,f)
    f.close()
    return

def courses():
    loop=True
    recLst=readFile() 
    while loop:
        displayLst(recLst)
        opt=input("<A>dd  <U>pdate  <D>delete     <Q>uit >> ").upper()
        if opt=="Q":
            loop=False
        elif opt=="A":
            recLst=addcourse(recLst)
            recLst.sort()
            saveFile(recLst)
        elif opt in ["U","D"]:
            recLst=delUpd(recLst,opt)
            recLst.sort()
            saveFile(recLst)
        else:
            print("Error.Please enter <A>, <U>, <D> or <Q>. Press enter to continue")
            input()
            os.system("cls")
            
if __name__=="__main__":            
    courses()
