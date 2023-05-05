#
# David Chong
# MADLIB GAME
# bigGame.py
#
#
# Prompts the user for a plural noun (PNOUN1)
# Prompts the user for a person's first name (FNAME)
# Prompts the user for a noun (NOUN1)
# Prompts the user for a person's last name (LNAME)
# Prompts the user for a second plural noun (PNOUN2)
# Prompts the user for a place (PLACE1)
# prompts the user for a third plural noun (PNOUN3)
# Prompts the user for another place (PLACE2)
# Prompts the user for a fourth plural noun (PNOUN4)
# Prompts the user for a second noun (NOUN2)
# Prompts the user for an adjective (ADJECTIVE1)
# Prompts the user for a second adjective (ADJECTIVE2)
# Prompts the user for a verb (VERB)
# Prompts the user for a third adjective (ADJECTIVE3)


def main():
    print("MadLib Game ...")
        
    PNOUN1 = input("Please enter a plural noun:")
            
    FNAME = input("Please enter a first name:")
               
    NOUN1 = input ("Please enter a noun:")
    
    LNAME = input("Please enter a last name:")
               
    PNOUN2 = input("Please enter a second plural noun:")
              
    PLACE1 = input("Please enter a place:")
             
    PNOUN3 = input("Please enter a third plural noun:")
    
    PLACE2 = input("Please enter a second place:")
             
    PNOUN4 = input("Please enter a fourth plural noun:")
    
    NOUN2 = input("Please enter a second noun:")
              
    ADJECTIVE1 = input("Please enter an adjective:")
        
    ADJECTIVE2 = input("Please enter a second adjective:")
              
    VERB = input("Please enter a verb:")
        
    ADJECTIVE3 = input("Please enter a third adjective:")
    
#Displays the story based on the data input

    print("The Big Game!!!")
    print("Hello there, sports",PNOUN1)
    print("This is",FNAME,"talking to you from the press",NOUN1)
    print("in",LNAME,"Stadium where 57,000 cheering",PNOUN2)
    print("have gathered to watch (the)",PLACE1, PNOUN3)
    print("take on (the)",PLACE2, PNOUN4)
    print("Even though the",NOUN2,"is shining, it’s a/an",ADJECTIVE1)
    print("cold day with the temperature in the",ADJECTIVE2,"20s.")
    print("We’ll be back for the opening",VERB,"-off after a few words")
    print("from our",ADJECTIVE3,"sponsor.")
    
main()















          
          
          
     
