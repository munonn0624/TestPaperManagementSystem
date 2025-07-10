#Module/Program name: P1G1student.py
#date created       : 16th March 2023
#created by         : Yu Xiao Shi
#import             : os(system clear screen), json
#modification       : check if got any repeated input,
#                     can skip an input if do not wish to update,
#                     student added will automatic arrange according the ascending order of the student ID order,
#                     screen will be clear if have invalid input before user can input data again


import os, json

def readFile():
    import json
    f=open("studprofile.txt","r")
    lst=json.load(f)
    lst.sort()
    f.close()
    return lst

def saveFile(recLst):
    import json
    f=open("studprofile.txt","w")
    json.dump(recLst,f)
    f.close()
    return        

def isdigit(studNRIC,studID,recID):
    status=True
    try:
        int(studNRIC,studID,recID)
    except:
        status=False
    return status

def displayLst(lst):
    f=open("studprofile.txt","r")
    print("-"*85)
    print("Student Maintenance")
    print("-"*85)
    if len(lst)==0:
        print("No records available")
    else:
        print(" Num    Student ID           Student Name                                 NRIC")
        print("-"*85)
        for i in range(len(lst)):
            print("%2s        %7s             %-40s%12s"%((i+1),lst[i][0],lst[i][1],lst[i][2]))
    print("-"*85)       

def delUpd(lst,opt):
    optLst=["U","D"]
    optDLst=["Modify","Delete"]
    cont="C"
    step=1
    while cont=="C":
        if step==1:
            idx=optLst.index(opt)
            os.system("cls")
            displayLst(lst)
            recID=input("Rec to <Q>uit >> ").upper()
            if recID=="Q":
                step=99
            elif not recID.isdigit():
                print("Invalid record number entered. Press enter to continue")
                input()
            else:
                recID=int(recID)
                num=[x[0] for x in lst]
                if recID>len(num):
                    print("Not enough data. Press enter to continue")
                    input()
                elif recID==0:
                    print("Wrong data. Press enter to continue")
                    input()
                else:
                    studID=lst[recID-1][0]
                    studName=lst[recID-1][1]
                    studNRIC=lst[recID-1][2]
                    step+=1
                    
        if step==2:
            os.system("cls")
            displayLst(lst)
            if opt=="D":
                print("Enter student ID <Q>uit      >> %7s"%studID)
                print("Enter student Name <Q>uit    >> %s"%studName)
                print("Enter student ID <Q>uit      >> %12s"%studNRIC)
                step=5
            else:
                print("Press <S> if do not wish to change this data")
                print("Record number                                >> %d"%recID)
                nstudID=input("Please enter 7 digit student ID <S>kip <Q>uit >>").upper()
                sLst=[x[0] for x in lst]
                if nstudID=="Q":
                    step=99
                elif nstudID=="S":
                    nstudID=studID
                    step +=1
                elif not nstudID.isdigit():
                    print("Data entered not a number. Press enter to continue")
                    input()
                elif not len(str(nstudID)) == 7:
                    print("Data entered not a 7 digit number. Press enter to continue")                    
                    input()
                else:
                    if nstudID in sLst:
                        print("Student ID repeated. Press enter to continue")
                        input()
                    else:
                        step= step+1
                    
        if step==3:
            os.system("cls")
            displayLst(lst)
            print("Press <S> if do not wish to change this data")
            print("Record number                                >> %d"%recID)
            print("Please enter student's ID <S>kip <Q>uit      >> %s"%nstudID)
            validCharacters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
            nstudName=input("Please enter student's name <S>kip <Q>uit >>").upper()
            sLst=[x[1] for x in lst]
            if nstudName=="Q":
                step=99
            elif nstudName.upper()=="S":
                nstudName=studName
                step +=1
            elif nstudName=="":
                print("Data entered cannot be blank. Press enter to continue")
                input()
            elif all(char in validCharacters for char in nstudName):
                if nstudName in sLst:
                    print("Student name repeated. Press enter to continue")
                    input()
                else:
                    step +=1
            else:
                print("Error with data entered.Please enter data without any digit or punctuation mark. Press enter to continue")
                input()
                
        if step==4:
            os.system("cls")
            displayLst(lst)
            print("Press <S> if do not wish to change this data")
            print("Record number                                >> %d"%recID)
            print("Please enter student's ID <S>kip <Q>uit      >> %s"%nstudID)
            print("Please enter student's name <S>kip <Q>uit    >> %s"%nstudName)
            nstudNRIC=input("Please enter 12 digit IC number without dash <S>kip <Q>uit >>").upper()
            sLst=[x[2] for x in lst]
            if nstudNRIC=="Q":
                step=99
            elif nstudNRIC.upper()=="S":
                nstudNRIC=studNRIC
                step +=1
            elif not str(nstudNRIC).isdigit():
                print("Data entered not a number. Press enter to continue")
                input()
            elif not len(str(nstudNRIC)) == 12:
                print("Data entered not a 12 digit number. Press enter to continue")
                input()
            else:
                if nstudNRIC in sLst:
                    print("Student NRIC repeated. Press enter to continue")
                    input()
                else:
                    step= step+1
                
        if step==5:
            if opt=="D":
                lst.pop(recID-1)
                print("Record deleted. Press enter to continue")
                input()
            else:
                os.system("cls")
                displayLst(lst)
                print("Record number    >> %d"%recID)
                print("Student ID       >> %s"%nstudID)
                print("Student Name     >> %s"%nstudName)
                print("Student NRIC     >> %s"%nstudNRIC)
                recID=int(recID)
                lst[recID-1]=[nstudID,nstudName,nstudNRIC]
                print("Record updated. Press enter to continue")
                input()
            step=1
            
        if step==99:
            os.system("cls")
            cont=False
    return lst               
            
def addstudent(lst):
    cont="C"
    step=1
    while cont=="C":
        if step==1:
            os.system("cls")
            displayLst(lst)
            studID=input("Please enter 7 digit student ID                   <Q>uit >> ")
            sLst=[x[0] for x in lst]
            if studID in ["Q","q"]:
                step=99
            elif not studID.isdigit():
                print("Data entered not a number. Press enter to continue")
                input()
            elif not len(str(studID)) == 7:
                print("Data entered not a 7 digit number. Press enter to continue")
                input()
            else:
                if studID in sLst:
                    print("Student ID repeated. Press enter to continue")
                    input()
                else:
                    step= step+1

        if step==2:
            os.system("cls")
            displayLst(lst)
            print("Please enter 7 digit student ID                   <Q>uit >> %s"%studID)
            validCharacters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
            studName=input("Please enter student's name                       <Q>uit >> ").upper()
            sLst=[x[1] for x in lst]
            if studName in ["Q","q"]:
                step=99
            elif studName=="":
                print("Data entered cannot be blank. Press enter to continue")
                input()
            elif all(char in validCharacters for char in studName):
                if studName in sLst:
                    print("Student name repeated. Press enter to continue")
                    input()
                else:
                    step +=1
            else:
                print("Error with data entered.Please enter data without any digit or punctuation mark. Press enter to continue.")
                input()

        if step==3:
            os.system("cls")
            displayLst(lst)
            print("Please enter 7 digit student ID                   <Q>uit >> %s"%studID)
            print("Please enter student's name                       <Q>uit >> %s"%studName)
            studNRIC=input("Please enter 12 digit IC number without dash      <Q>uit >> ")
            sLst=[x[2] for x in lst]
            if studNRIC in ["Q","q"]:
                step=99
            elif not str(studNRIC).isdigit():
                print("Data entered not a number. Press enter to continue.")
                input()
            elif not len(str(studNRIC)) == 12:
                print("Data entered not a 12 digit number. Press enter to continue.")
                input()
            else:
                if studNRIC in sLst:
                    print("Student NRIC repeated. Press enter to continue")
                    input()
                else:
                    step= step+1

        if step==4:
            os.system("cls")
            displayLst(lst)
            print("Student ID       >> %s"%studID)
            print("Student Name     >> %s"%studName)
            print("Student NRIC     >> %s"%studNRIC)
            print("Record added. Press enter to continue")
            input()
            lst.append([studID, studName, studNRIC])
            f=open("studprofile.txt","a")
            f.write(str(lst.append))
            f.close()
            os.system("cls")
            return lst
        
        if step==99:
            os.system("cls")
            cont=False
    return lst

def student():
    loop=True
    recLst=readFile()
    while loop:
        displayLst(recLst)
        opt=input("<A>dd  <U>pdate  <D>delete     <Q>uit >> ").upper()
        if opt=="Q":
            loop=False
        elif opt=="A":
            recLst=addstudent(recLst)
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
    student()

