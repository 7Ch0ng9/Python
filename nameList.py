#nameList.py
#November 16, 2021
#This program demonstrates a simple list
def main():
    #list of names, size 5, strings
    nameList = ["", "", "","", ""]

    #assign the first name in the list
    nameList[0] = "Jennifer"

    #assign the second name in the list
    nameList[1] = "Jonathan"

    #prompt the user for all five names
    for i in range(5):
        #prompt
        nameList[i] = input("Enter a name "+ str(i + 1) + ": ")
        
    #for loop to display the data
    for i in range(5):
        print(str(i + 1) + ": " + nameList[i])

