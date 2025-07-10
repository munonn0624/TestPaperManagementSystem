#Module/Program name:P1G1generate.py
#date created       :17th March 2023
#created by         :Ngu Kiong Xiong
#import             :os(system clear screen), json, random
#modification       :Clear screen(clear the error message before input again),
#                    read file from generated file,
#                    testdate manually input

import os, json, random

def genemain():
    os.system("cls")
    step=1
    fCourses=openFile("courses","r")
    student=openFile("studprofile","r")
    question=openFile("quesbank","r")
    bLst=[]
    loop=True
    while loop:
        if step==1:
            print("-"*65)
            print("Generate/Create Student Course Test Paper  <E>Exit")
            print("-"*65)
            courID=([i[0] for i in fCourses])
            courID2=",".join(courID)
            print("["+courID2+"]")
            step+=1   
                    
        if step==2:
            courses=input("course ID <Q>uit >>").upper()
            recCour=[x[1] for x in fCourses]
            recID=[x[0] for x in fCourses]
            if courses=="Q":
                os.system("cls")
                step=99
                
            elif courses in recID:
                os.system("cls")
                step+=1
            else:
                print("Invalid Course ID entered,Please Press Enter To Continue")
                input()
                os.system("cls")
                step=1

        if step==3:
            index=recID.index(courses)
            print("Generating Test File -->")
            print("Course ID : %s (%s)"%(courses,recCour[index]))
            print()
            print("-"*65)
            print("Student List")
            print("-"*65)
            print("StudID   StudName                                 NRIC Number")
            print("-"*65)
            for i in range(len(student)):   
                print("%s  %-40s %s"%(student[i][0],student[i][1],student[i][2]))

            studId=input("Student ID (YY#####)     <Q>uit >> ").upper()
            recname=[x[1] for x in student]
            recStudId=[x[0] for x in student]
            if studId=="Q":
                os.system("cls")
                step=1
                
            elif studId in recStudId:
                os.system("cls")
                step+=1

            else:
                print("Invalid Student ID Entered,Please Press Enter To Continue")
                input()
                os.system("cls")
                        
        if step==4:
            os.system("cls")
            mthLst=[0,31,28,31,30,31,30,31,31,30,31,30,31]
            index2=recStudId.index(studId)
            print("Generating Test File -->")
            print("Course ID : %s (%s)"%(courses,recCour[index]))
            print("StudentID : %s  (%s)"%(studId,recname[index2]))
            print()
            print("-"*65)
            print("Test Date Setup - Available slots")
            print("-"*65)
            print("Course ID : %s (%s)--->"%(courses,recCour[index]))
            print("Number of questions(Size)")
            print("-"*65)
            testDate=input("TestDates(dd/mm/yyyy)                      <Q>uit >> ").upper()
            if testDate=="Q":
                os.system("cls")
                step=3
            elif testDate=="00/00/0000":
                print("Invalid Testdate Entered,Please Press Enter To Continue")
                input()
            
            elif not testDate[0:2].isdigit():  
                print("Invalid Format For Testdate Entered,Please Press Enter To Continue")
                input()

            elif not testDate[3:5].isdigit(): 
                print("Invalid Format For Testdate Entered,Please Press Enter To Continue")
                input()

            elif not testDate[6:10].isdigit(): 
                print("Invalid Format For Testdate Entered,Please Press Enter To Continue")
                input() 
    
            elif len(testDate)!=10:
                print("Invalid Length Of Testdate Entered,Please Press Enter To Continue")
                input()
               
            elif (testDate[2] and testDate[5])!="/":
                print("Invalid Format For Testdate Entered,Please Press Enter To Continue")
                input()

            elif int(testDate[3:5])>12:
                print("Invalid Testdate Entered,Please Press Enter To Continue")
                input()
               
            elif int(testDate[:2]) > mthLst[int(testDate[3:5])]:
                print("Invalid Testdate Entered,Please Press Enter To Continue")
                input()
            
            else:
               step+=1

        if step==5:
            os.system("cls")
            index2=recStudId.index(studId)
            print("Generating Test File -->")
            print("Course ID : %s (%s)"%(courses,recCour[index]))
            print("StudentID : %s  (%s)"%(studId,recname[index2]))
            print()
            print("-"*65)
            print("Test Date Setup - Available slots")
            print("-"*65)
            print("Course ID : %s (%s)--->"%(courses,recCour[index]))
            print("Number of questions(Size)")
            print("-"*65)
            print("TestDates(dd/mm/yyyy)                      <Q>uit >> %s"%(testDate))
            slot=input("Slots                                             >> ")
            if not slot.isdigit():
                print("Data entered not a number. Press enter to continue")
                input()
                os.system("cls")
            elif slot=="0":
                print("Slot unavailable. Press enter to continue")
                input()
                os.system("cls")
    
            else:
                step+=1
                
        if step==6:
            os.system("cls")
            index2=recStudId.index(studId)
            print("Generating Test File -->")
            print("Course ID : %s (%s)"%(courses,recCour[index]))
            print("StudentID : %s  (%s)"%(studId,recname[index2]))
            print()
            print("-"*65)
            print("Test Date Setup - Available slots")
            print("-"*65)
            print("Course ID : %s (%s)--->"%(courses,recCour[index]))
            print("Number of questions(Size)")
            print("-"*65)
            print("TestDates(dd/mm/yyyy)                      <Q>uit >> %s"%(testDate))
            print("Slots                                             >> %s"%(slot))
            numQues=input("Number of questions want to assign                >> ")
            code=[x[0]for x in question]
            if not numQues.isdigit():
                print("Data entered not a number. Press enter to continue")
                input()
                os.system("cls")

            elif numQues=="0":
                print("Unable To Generate.Please Press Enter To Continue")
                input()
                os.system("cls")
                
            elif code.count(courses)==0:
                print("No Question For This Course,Please Press Enter To Continue")
                input()
                os.system("cls")
                
            elif int(numQues) > code.count(courses):
                print("Not Enough Questions In The Question Bank For This Course,Please Press Enter To Continue")
                input()
                os.system("cls")
                
            else:
                os.system("cls")
                step+=1

        if step==7:
            print("Generating Test File -->")
            print("Course ID : %s (%s)"%(courses,recCour[index]))
            print("StudentID : %s  (%s)"%(studId,recname[index2]))
            print("TestDate  : %s(Slots:%s Ques Size: %s)"%(testDate,slot,numQues))
            print()
            generate=input("Generate <Y>es/<N>o      <Q>uit >> ").upper()
            for line in question:
                if line[0]==courses:
                    bLst.append(line)
            if generate=="Q":
                os.system("cls")
                print("-"*65)
                print("Test Date Setup - Available slots")
                print("-"*65)
                print("Course ID : %s (%s)--->"%(courses,recCour[index]))
                print("Number of questions(Size)")
                print("-"*65)
                step=4
            elif generate=="Y":
                os.system("cls")
                newFile=open("%s %s"%(courses,studId),"a")
                mystr=""
                mystr +="Course ID : %s (%s)"%(courses,recCour[index])+"\n"
                mystr +="StudentID : %s  (%s)"%(studId,recname[index2])+"\n"
                mystr +="TestDate  : %s (Slots:%s Ques Size: %s)"%(testDate,slot,numQues)+"\n\n"
                cLst=random.sample(bLst,int(numQues))
                for i in range(len(cLst)):
                    mystr +="Q%d."%(i+1)+"%s"%cLst[i][1]+"\n"
                    mystr +="%s\n%s\n%s\n%s"%(cLst[i][2],cLst[i][3],cLst[i][4],cLst[i][5])+"\n\n"
                newFile.write(mystr)
                newFile.close()
                print("File Generated...")
                print()
                step+=1
            elif generate=="N":
                print("File Not Generated,Press Enter To Mainmenu")
                input()
                step=99
            else:
                print("Invalid Option Entered,Please Press Enter To Continue")
                input()
                os.system("cls")
                print()
                
        if step==8:
            print("Generating Test File -->")
            print("Course ID : %s (%s)"%(courses,recCour[index]))
            print("StudentID : %s  (%s)"%(studId,recname[index2]))
            print("TestDate  : %s(Slots:%s Ques Size: %s)"%(testDate,slot,numQues))
            print()
            print("Generate <Y>es/<N>o      <Q>uit >> %s"%(generate))
            print("File Generated...")
            lookFile=input("Do You Want To Look The File? <Y>es/<N>o >> ").upper()
            if lookFile=="Y":
                os.system("cls")
                f=open("%s %s"%(courses,studId),"r")
                txt=f.read()
                f.close()
                print(txt)
                print("Generate Successfully, Press Enter To Mainmenu")
                input()
                step=99
            elif lookFile=="N":
                print("Thanks For Generating Paper By This System,Press Enter To Mainmenu")
                input()
                step=99
            else:
                print("Invalid Option Entered,Please Press Enter To Continue")
                input()
                os.system("cls")

        if step==99:
            loop=False

            
def openFile(fileName,mode):
    f=open(fileName+".txt",mode)
    lst=json.load(f)
    f.close()
    return lst

if __name__=="__main__":     
    genemain()
            

