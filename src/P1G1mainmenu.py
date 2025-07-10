#Module/Program name:P1G1mainmenu.py
#date created       :17th March 2023
#created by         :Lee Wei Jin, Yu Xiao Shi, Lee Mun Onn
#import             :os(system clear screen)
#modification       :screen will be clear if have invalid input before user can input data again


import os
import P1G1student as stud
import P1G1course as course
import P1G1qbank as bank
import P1G1generate as generate

def mainmenu():
    cont1="C"
    while cont1=="C":
        os.system("cls")
        print("-"*65)
        print("Test Management System --> Process Steps")
        print("-"*65)
        print("<1>Setup\n"+"<2>Generate Test Paper\n"+"<E>xit\n",end="")
        opt=input("option >>").upper()
        if opt=="1":
            mainask()
        elif opt=="2":
            generate.genemain()
        elif opt=="E":
            print ("\nThank you for using the system\nPlease press enter to close the program.")
            input()
            cont1="Q"
        else:
            print("\tError.Please enter <1>,<2>,<E>. Press enter to continue")
            input()
    os.system("cls")

def mainask():
    cont2="C"
    while cont2=="C":
        os.system("cls")
        print("-"*65)
        print("System Configuration -> Process steps")
        print("-"*65)
        opt1=input("<1>Student <2>Courses <3>Question Bank   <E>xit:").upper()
        if opt1=="1":
            os.system("cls")
            stud.student()
        elif opt1=="2":
            os.system("cls")
            course.courses()
        elif opt1=="3":
            os.system("cls")
            bank.displaymain()
        elif opt1=="E":
            cont2="Q"
        else:
            print("\tError.Please enter <1>,<2>,<3>,<E>. Press enter to continue")
            input()
mainmenu()
