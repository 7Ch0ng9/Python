#fileAppendExample.py
#November 7, 2021
#This program demonstrates how to append data to a text file.

def main():
    #declare variables
    #string fName, lName
    fName = ""
    lName = ""
    #float grade1, grade2, grade3
    grade1 = grade2 = grade3 = 0.0

    #Intro
    print("WELCOME TO THE GRADE DATABASE PROGRAM!!\n")

    #Prompt for data
    fName = input("Enter a student first name: ")
    lName = input("Enter a student last name: ")
    grade1 = float(input("Enter grade 1: "))
    grade2 = float(input("Enter grade 2: "))
    grade3 = float(input("Enter grade 3: "))
    
    #open file for appending ("a") When you use "a" this will create the file if it does not yet exist and will add to the file if it does
    outfile = open("grades.txt", "a")
    #process data - write to the file - comma delimit the file.  A delimiter is a character that separates the fields in a record.
    outfile.write(fName + "," + lName + "," + str(grade1) + "," + str(grade2) + "," + str(grade3) + "\n")
    #close file
    outfile.close()
