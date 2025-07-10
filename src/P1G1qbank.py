#Module/Programs name: P1G1qbank.py
#date created        : 23th March 2023
#created by          : Lee Mun Onn
#import              : os, json
#Modification        : Skip if do not wish to update question/option A,B,C,D
#                      or answer, clear screen (after any invalid inputed)
 

import os, json

def displaymain():
    clst=readFile2()
    loop=True
    while loop:
       os.system("cls")
       print("-"*65)
       print("Question Bank Maintainance")
       print("-"*65)
       
       ccodelst=[]
       for i in range(len(clst)):
           ccode=clst[i][0]
           ccodelst.append(ccode)

       ncStr=", ".join(ccodelst)
       print("[ "+ncStr+" ]")
           
       cID=input("course ID <Q>uit >> ").upper()
       if cID=="Q":
          loop=False
          os.system("cls")
       elif not len(cID)==8:
          print("Course ID must have 4 alphabets follow by 4 digits. Press enter to return.")
          input()
       elif not cID[4:8].isdigit(): 
          print("Course ID entered must end with 4 digits. Press enter to return.")
          input()
       elif not cID[:4].isalpha():
          print("Course ID entered must start with 4 alphabets. Press enter to return.")
          input()
       elif not cID in ccodelst:
           print("Invalid course code entered. Press enter to return.")
           input()
       else:
          qbank(clst,cID)    


def displayLst(reclst,clst,cID):
    print("-"*120)
    print("Question Bank Maintainance")
    print("-"*120)
    for c in clst:
        if c[0]==cID:
            cDesc=c[1]
    print("%s (%s)--->"%(cID,cDesc))
    print("-"*120)
    print("No.   Question")
    print("-"*120)

    findQues=False

    for p in reclst:
        if cID == p[0]:
            findQues= True
              
    if not findQues:
        print("No questions for this course found")

    else:
        dispNum=1
        for a in reclst:
            if a[0]==cID:
                qdisp=a[1]
                print("%2d    %s"%(dispNum,qdisp))
                dispNum+=1
            
           
    print("-"*120)

def UDques(lst,opt,cID):
    clst=readFile2()
    reclst=readFile()
    optLst =["U","D"]
    optDLst=["Modify","Delete"]
    udLst=[]
    idx = 0
    while idx < len(lst):
        if lst[idx][0] == cID:
            udLst.append(lst.pop(idx))
        else:
            idx += 1
    cont="C"
    step=1
    while cont=="C":  
        if step==1:
            os.system("cls")
            displayLst(reclst,clst,cID)
            idx=optLst.index(opt)
            rec=input("Enter question number wish to perform    <B>ack >> ").upper()
            if rec=="B":
                step=99
            elif not rec.isdigit():
                print("Invalid question number entered. Press enter to return.")
                input()
            elif int(rec) not in range(1,len(udLst)+1):
                print("Question number does not exist. Press enter to return.")
                input()
            else:
                rec=int(rec)
                ques, optA, optB, optC, optD, ans = udLst[rec-1][1:]
                step +=1
                
        if step==2:
            os.system("cls")
            print("Updating Question %d..."%rec)
            print()
            print(ques)
            print(optA)
            print(optB)
            print(optC)
            print(optD)
            
            if opt=="D":
                step=6
            else:
                print("Answer : "+ans)
                print()
                print("Press <S> if do not wish to change this data")
                nques=input("Enter new question <S>kip <Q>uit >> ")
                if nques in ["Q","q"]:
                    step=99
                elif nques.upper()=="S":
                    nques=ques
                    step +=1
                elif nques=="":
                    print("Invalid data entered. Press enter to return.")
                    input()
                else:
                    step +=1
                
        if step==3:
            os.system("cls")
            cnt=0
            
            while cnt < 4:
                os.system("cls")
                print("Updating Question %d..."%rec)
                print()
                print(ques)
                print(optA)
                print(optB)
                print(optC)
                print(optD)
                print("Answer : "+ans)
                print()
                if cnt == 0:
                    print("Press <S> if do not wish to change this data")
                    print("Enter new question          <Q>uit  >> %s"%nques)
                    noptA = input("Enter new option A          <S>kip  >> ")
                    if noptA == "":
                        print("Please enter an answer for option A. Press enter to return.")
                        input()
                    elif noptA.upper()=="S":
                        optA=optA
                        noptA=optA[3:]
                        cnt+=1
                    else:
                        cnt += 1
                elif cnt == 1:
                    print("Press <S> if do not wish to change this data")
                    print("Enter new question          <Q>uit  >> %s"%nques)
                    print("Enter new option A          <S>kip  >> %s"%noptA)
                    noptB = input("Enter new option B          <S>kip  >> ")
                    if noptB == "":
                        print("Please enter an answer for option B. Press enter to return.")
                        input()
                    elif noptB.upper()=="S":
                        optB=optB
                        noptB=optB[3:]
                        cnt+=1
                    else:
                        cnt += 1
                elif cnt == 2:
                    print("Press <S> if do not wish to change this data")
                    print("Enter new question          <Q>uit  >> %s"%nques)
                    print("Enter new option A          <S>kip  >> %s"%noptA)
                    print("Enter new option B          <S>kip  >> %s"%noptB)
                    noptC = input("Enter new option C          <S>kip  >> ")
                    if noptC == "":
                        print("Please enter an answer for option C. Press enter to return.")
                        input()
                    elif noptC.upper()=="S":
                        optC=optC
                        noptC=optC[3:]
                        cnt+=1
                    else:
                        cnt += 1
                elif cnt == 3:
                    print("Press <S> if do not wish to change this data")
                    print("Enter new question          <Q>uit  >> %s"%nques)
                    print("Enter new option A          <S>kip  >> %s"%noptA)
                    print("Enter new option B          <S>kip  >> %s"%noptB)
                    print("Enter new option C          <S>kip  >> %s"%noptC)
                    noptD = input("Enter new option D          <S>kip  >> ")
                    if noptD == "":
                        print("Please enter an answer for option D. Press enter to return.")
                        input()
                    elif noptD.upper()=="S":
                        optD=optD
                        noptD=optD[3:]
                        cnt+=1
                    else:
                        cnt+=1
            step+=1
                            
        if step==4:
            os.system("cls")
            print("Updating Question %d..."%rec)
            print()
            print(ques)
            print(optA)
            print(optB)
            print(optC)
            print(optD)
            print("Answer : "+ans)
            print()
            print("Enter new question          <Q>uit  >> %s"%nques)
            print("Enter new option A                  >> %s"%noptA)
            print("Enter new option B                  >> %s"%noptB)
            print("Enter new option C                  >> %s"%noptC)
            print("Enter new option D                  >> %s"%noptD)
            confirm= input("Confirm your input (Y/N) <Q>uit >> ").upper()
            if confirm=="Q":
                step=99
            elif confirm=="":
                print("Invalid data entered. Press enter to return")
                input()
            elif not confirm.isalpha():
                print("Invalid data entered. Please enter (Y/N). Press enter to return.")
                input()
            elif confirm=="N":
                print("Question entered is not saved. Press enter to return.")
                input()
                step=99
            elif confirm=="Y":
                step +=1
            else:
                print("Invalid data entered. Press enter to return")
                input()
            
        if step==5:
            os.system("cls")
            print("Updating Question %d..."%rec)
            print()
            print(ques)
            print(optA)
            print(optB)
            print(optC)
            print(optD)
            print("Answer : "+ans)
            print()
            print("Enter new question          <Q>uit  >> %s"%nques)
            print("Enter new option A                  >> %s"%noptA)
            print("Enter new option B                  >> %s"%noptB)
            print("Enter new option C                  >> %s"%noptC)
            print("Enter new option D                  >> %s"%noptD)
            print("Confirm your input (Y/N)     <Q>uit >> %s"%confirm)
            print("Press <S> if do not wish to change this data")
            nans=input("Enter new answer <ABCD>     <S>kip <B>ack >> ").upper()
            if nans=="B":
                step=99
            elif nans=="S":
                nans=ans
                step+=1
            elif not nans.isalpha():
                print("Invalid answer entered. Press enter to return")
                input()
            elif not nans in ["A","B","C","D","S"]:
                print("Invalid answer entered. Press enter to return")
                input()
            else:
                print()
                print("Update Successfully!!! Press enter to return")
                input()
                step +=1

            
            
        if step==6:
            os.system("cls")
            displayLst(reclst,clst,cID)
            if opt=="D":
                print("Deleting Question %d..."%rec)
                print()
                valid=input("Are you sure you want to delete this question? (Y/N)  >> ").upper()
                if valid == "Y":
                    udLst.pop(rec-1)
                    print()
                    print("Question is deleted... Press enter to return")
                    input()
                    step=99
                elif valid == "N":
                    print("Question is not deleted.")
                    step=99
                else:
                    print("Invalid data entered. Please enter (Y/N). Press enter to return")
                    input()
            else:
                recID=int(rec)
                wNoptA="A. %s"%noptA
                wNoptB="B. %s"%noptB
                wNoptC="C. %s"%noptC
                wNoptD="D. %s"%noptD
                udLst[rec-1]=[cID,nques, wNoptA,wNoptB,wNoptC,wNoptD,nans]
                print("Record updated... Press enter to continue")
                input()
                step=99
                
        if step==99:
            lst.extend(udLst)
            cont="Q"
            os.system("cls")
    return lst

def addQues(lst,cID):
    clst=readFile2()
    reclst=readFile()
    validLst=[]
    idx = 0
    while idx < len(lst):
        if lst[idx][0] == cID:
            validLst.append(lst.pop(idx))
        else:
            idx += 1

    cont="C"
    step=1
    while cont=="C":
        if step==1:
            os.system("cls")
            displayLst(reclst,clst,cID)
            qnum=    input("Question number          <Q>uit >> ").upper()
            if qnum=="Q":
                step=99
            elif not qnum.isdigit():
                print("Invalid question number entered. Press enter to return.")
                input()
            elif qnum=="0":
                print("Invalid question number entered. Press enter to return.")
                input()
            elif int(qnum) in range(1,len(validLst)+1):
                print("Question number already existed. Press enter to return.")
                input()
            elif int(qnum) > len(validLst)+1:
                print("The added question must be the next number of the last question.")
                print("Press enter to return")
                input()
            else:
                step +=1
                
        if step==2:
            os.system("cls")
            displayLst(reclst,clst,cID)
            print("Question number          <Q>uit >> %s"%qnum)
            ques=    input("Enter question           <Q>uit >> ")
            if ques in["Q","q"]:
                step=1
            elif ques=="":
                print("Invalid question entered. Press enter to return.")
                input()
            else:
                step +=1
                
        if step==3:
            cnt=0
            while cnt < 4:
                os.system("cls")
                displayLst(reclst,clst,cID)
                print("Question number          <Q>uit >> %s"%qnum)
                print("Enter question           <Q>uit >> %s"%ques)
                if cnt == 0:
                    optA=input("Enter option A                  >> ")
                    if optA == "":
                        print("Please enter an answer for option A. Press enter to return.")
                        input()
                    else:
                        cnt += 1
                elif cnt == 1:
                    print("Enter option A                  >> %s"%optA)
                    optB=input("Enter option B                  >> ")
                    if optB == "":
                        print("Please enter an answer for option B. Press enter to return.")
                        input()
                    else:
                        cnt += 1
                elif cnt == 2:
                    print("Enter option A                  >> %s"%optA)
                    print("Enter option B                  >> %s"%optB)
                    optC=input("Enter option C                  >> ")
                    if optC == "":
                        print("Please enter an answer for option C. Press enter to return.")
                        input()
                    else:
                        cnt += 1
                elif cnt == 3:
                    print("Enter option A                  >> %s"%optA)
                    print("Enter option B                  >> %s"%optB)
                    print("Enter option C                  >> %s"%optC)
                    optD=input("Enter option D                  >> ")
                    if optD == "":
                        print("Please enter an answer for option D. Press enter to return.")
                        input()
                    else:
                        cnt+=1           
            
            step +=1
            
        if step==4:
            os.system("cls")
            displayLst(reclst,clst,cID)
            print("Question number          <Q>uit >> %s"%qnum)
            print("Enter question           <Q>uit >> %s"%ques)
            print("Enter option A                  >> %s"%optA)
            print("Enter option B                  >> %s"%optB)
            print("Enter option C                  >> %s"%optC)
            print("Enter option D                  >> %s"%optD)
            confirm= input("Confirm your input (Y/N) <Q>uit >> ").upper()
            if confirm=="Q":
                step=99
            elif not confirm.isalpha():
                print("Invalid entered. Press enter to return")
                input()
            elif confirm=="N":
                print("Question entered is not saved. Press enter to return.")
                input()
                step=99
            elif confirm=="Y":
                step +=1
            else:
                print("Invalid data entered. Please enter (Y/N). Press enter to return")
                input()

        if step==5:
            os.system("cls")
            displayLst(reclst,clst,cID)
            print("Question number          <Q>uit >> %s"%qnum)
            print("Question number          <Q>uit >> %s"%ques)
            print("Enter option A                  >> %s"%optA)
            print("Enter option B                  >> %s"%optB)
            print("Enter option C                  >> %s"%optC)
            print("Enter option D                  >> %s"%optD)
            print("Confirm your input (Y/N) <Q>uit >> %s"%confirm)
            ans=     input("Answer <ABCD>     <S>kip <Q>uit >> ").upper()
            if ans=="Q":
                step=99
            elif not ans.isalpha():
                print("Invalid answer entered. Press enter to return")
                input()
            elif ans in ["A","B","C","D","S"]:
                print()
                print("Question is added... Press enter to return")
                input()
                step +=1
            else:
                print("Invalid answer entered. Press enter to return")
                input()

        if step==6:
            woptA="A. %s"%optA
            woptB="B. %s"%optB
            woptC="C. %s"%optC
            woptD="D. %s"%optD
            lst.extend(validLst)
            lst.append([cID,ques,woptA,woptB,woptC,woptD,ans])
            f=open("quesbank.txt","a")
            f.write(str(lst.append))
            f.close()
            os.system("cls")
            return lst
            
        if step==99:
            lst.extend(validLst)
            os.system("cls")
            cont="Q"
    return lst
   
def readFile():
    import json
    f=open("quesbank.txt","r")
    reclst=json.load(f)
    f.close()
    return reclst

def readFile2():
    import json
    f=open("courses.txt","r")
    clst=json.load(f)
    f.close()
    return clst

def saveFile(recLst):
    import json
    f=open("quesbank.txt","w")
    json.dump(recLst,f)
    f.close()
    return

def qbank(clst,cID):
    loop=True
    recLst=readFile()   
    while loop:
        os.system("cls")
        displayLst(recLst,clst,cID)
        opt=input("<A>dd  <U>pdate  <D>delete                <Q>uit  >> ").upper()
        if opt=="Q":
            loop=False
        elif opt=="A":
            recLst=addQues(recLst,cID)
            saveFile(recLst)
        elif opt in ["U","D"]:
            recLst=UDques(recLst,opt,cID)
            saveFile(recLst)
        else:
            print("Error in option entered. Please enter <A>,<U>,<D>,<Q>. Press enter to return")
            input()

if __name__=="__main__":
    displaymain()
