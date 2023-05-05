# guessNumber.py
# David Chong
# October 23,2021
# This program generates a random number in the range 1 through 100. The program
# promts the user to guess the random number. The program will validate the number
# entered to ensure it is in the range of 1-100. The program will compare the user's 
# guess to the mystery number and provide feedback, "too high or "too low"
# The game will also "congratulate" the player if the user's guess is the same as
# the mystery number generated. The user has 7 rounds per game to guess
# the correct number, the user can play as many times as they wish.

# Import statement for random number generator 
import random


def main():
    randomNumber = 0
    again = "y"
    while again == "y":
        # Initialize variables used in program
        randomNumber = random.randrange(1, 100)
        print(randomNumber)
        count = 0
        userGuess = False
            
        # Display Intro
        print()
        print("Guess the Mystery Number ...")
        print()
        count = count + 1
        
        # Amount of rounds per game    
        while count < 8 and userGuess != randomNumber:
            # Prompt user for number
            print("Round", count, "of 7")
            print("------------------")
            userGuess = int(input("Enter your guess (1-100): "))
            count = count + 1

            # Varifies number is valid range
            while userGuess < 1 or userGuess > 100:
                print("Error ... Incorrect number. Try Again")
                userGuess = int(input("Enter your guess (1-100): "))                      
                                
            # Compares number against the player's guess   
            if userGuess < randomNumber:
                print("--->", userGuess, "is too Low ...")
                print()
                
            elif userGuess > randomNumber:
                print("--->", userGuess, "is too High ...")
                print()
                           
            else:
                userGuess == True
                print()
                print("Congratulations ... You guessed the Mystery Number!")
                print()
        # Option to play again
        again = input("Would you like to try again? y/n: ")
        print(again)
        
               
    # Option to exit The Guessing Game                                        
    print("You Have Ended The Guessing Game!")
    print()
               

   
            
            
         


            
    
            
                
        
            
                       
             
