# vingtEtUn.py
# David Chong
# November 21, 2021
# Vingt-et-un is a dice game (known as Blackjack in the USA), where a player competes against the computer (house).
# The goal of the game is to score 21 points, or as near as possible without going over.
# The two players take turns throwing two dies as many times as desired and adding up the numbers thrown on each round.
# A player who totals over 21 is bust and loses the game.The player whose total is nearest 21, after each player
# has had a turn, wins the game. In the case of an equality high total, the game is tied.
# The game is over at the end of a round when: One or both players are bust. Both players choose to stay.
# Notes: Once a player totals 14 or more, one of the dies is discarded for the consecutive turns.
# The house must throw the dice until the total is 17 or higher. At 17 or higher, the house must stay.
            
            
# Import statement for random number generator
import random
# Import statement to pause game while rolling dice 
import time

def main():
    Player = 0
    House = 0
    Player_stay = False
    House_stay = False
    choice = ""
    roll_again = "y"
    play_again = "y"
    
    # Menu Options   
    while choice != "3":
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("*Choose what you would like to do from the following menu *")
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print()
        print("1: Read the rules for Ving-Et-Un")
        print("2: Play the game Ving-Et-Un")
        print("3: Exit")
        print()
        choice = input()
        # Rules of Vingt-Et-Un                    
        if choice == "1" :
            print("Option:[1]")
            # Display Rules
            print("Vingt-et-un is a dice game (known as Blackjack in the USA), where a")
            print("player competes against the computer (house).The goal of the game is")
            print("to score 21 points, or as near as possible without going over.")
            print("The two players take turns throwing two dies as many times as desired")
            print("and adding up the numbers thrown on each round.A player who totals over 21")
            print("is bust and loses the game.The player whose total is nearest 21, after each player")
            print("has had a turn, wins the game. In the case of an equality high total, the game is tied.")
            print("The game is over at the end of a round when: One or both players are bust.")
            print("Both players choose to stay.")
            print("Notes: Once a player totals 14 or more, one of the dies is discarded for the consecutive turns.")
            print("The house must throw the dice until the total is 17 or higher. At 17 or higher, the house must stay.")
            print()
         # Starts Vingt-Et-Un game   
        if choice == "2" :
               print("Option[2]")
               # Play The Game Vingt-Et-Un Intro
               print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
               print("You are starting Ving-Et-Un ...")
               print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
               print("-------------------------------")
               print("---------*Vingt*---------------")
               print("-------------*Et*--------------")
               print("---------------*Un*------------")
               print("-------------------------------")
               print("*-*-*-*-*-Good Luck!*-*-*-*-*-*")
               print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
               print()
               playGame()
    # Exit Game           
    if choice == "3":
      print("Option:[3]")
      print("............................")
      print("Exiting the Vingt-Et-Un Game")
      print("Goodbye!")
      print("............................")


def playGame():
    # PLayer's Name
    name = input("Enter your name: ")
    print("..............................")
    print(name,"Let's play Vingt-Et-Un!")
    print("..............................")
    # Initialize variables
    Player = 0
    House = 0
    # Choice of House and Player
    Player_stay = False
    House_stay = False
    roll_again = "n"
    count = 1
        
    while True:        
        # Initialize variables for game
        print()
        print("^^^^^^^^^^^^^^^^^^^^")
        print("Rolling the Dice ...")
        print("^^^^^^^^^^^^^^^^^^^^")
        print()
        time.sleep(1)# Pause while rolling dice    
        die1 = random.randint (1, 6)
        die2 = random.randint (1, 6)
        # House has to Stay if point total is 17 or more        
        if House >= 17:
            print("The House score is: ", "[", House,"]", "The House chooses to STAY ...")
            print()
            print("House total is:", "[",House,"]")
            House_stay = True        
        # Rolls only ONE die if point total is 14 or more
        elif House >= 14:
            die1 = random.randint (1, 6)
            die2 = 0
            print()
            print("The House can roll with only ONE die.")
            print(".....................................")
            print("The House rolled a:", "[",die1,"]")
            print(".....................................")
            print()
            House += die1 + die2
            print("The House total so far is:", "[",House,"]")
            print()
        # Displays results of dice roll    
        else:
            print("The House rolled a:", "[",die1,"]" ,"\nand..............a:","[",die2,"]")
            print("...............................")             
            House += die1 + die2
            print()
            print("House score so far is", "[",House,"]")
            print("....................................")
            
            
            
        # Display  House results according to score
        if House > 21 and Player < 22:
            print("BUST! ... House LOST ... ","[", name, "]", "is the WINNER!!!\n")
        if House > 21:
            print("The House went over [ 21 ] ...")
            print("The House score is:", "[",House,"]")
            print("[", name,"]" "is the WINNER !!!\n")
        if House < 22 and Player > 21:
            print("BUST! ...", "[", name, "]", "LOST ... House is the WINNER !!!\n") 
        elif House == 21:
            print("Congratulations! House! ... Vingt-Et-Un ... YOU ARE THE WINNER !!!\n")
            print()
            print("The Game is Over ... House WINS !!! ")
            print()
            play_again = "y"
            main()
            play_again = input("Do you want to play Vingt-Et-Un again? (y/n) ").lower()
            print("")
        # Display House and Player results if both decide to Stay
        if House_stay and Player_stay:
            if Player > House and Player < 21 and House < 21:
                print("House LOST ...","[", name, "]","is the WINNER !!!\n")
            elif House > Player and House < 21 and Player < 21:
                print("[",name,"]","LOST ... House is the WINNER !!!\n")    
            elif Player > 21 and House < 21:
                print("BUST! ...", "[", name, "]", "LOST ... House is the WINNER !!!\n")  
            elif House > Player and Player == 21:
                print("BUST! ... House LOST ...","[",name,"]","is the WINNER !!!\n")
            elif Player > House and House == 21:
                print("BUST! ... ","[",name,"]", "LOST ... House is the WINNER !!!\n")
            elif House == 21:
                print("Congratulations! House! ... Vingt-Et-Un ... YOU ARE THE WINNER !!!\n")
            elif House == 21 and Player == 21:
                print("Game Over! ... Its a TIE !!!\n")
                print("")
            play_again = "n"
            main()
            play_again = input("Do you want to play Vingt-Et-Un again? (y/n) ").lower()
        print()
        roll_again = "n"
        roll_again = input("Do you want to ROLL ... (y) or STAY ... (n)? (y/n) ").lower()
        print()
        if roll_again == "y":
            # Initialize variables for game
            time.sleep(1)# Pause while rolling dice    
            die1 = random.randint (1, 6)
            die2 = random.randint (1, 6)
            # Roll ONE die if point total is 14 or more              
            if Player >= 14:
                time.sleep(1)# Pause while rolling dice
                die1 = random.randint (1, 6)
                die2 = 0
                print("[",name,"]", "You can roll with only ONE die ...")
                print("............................................")
                input("Hit enter to continue")
                print("............................................")
                print("[",name,"]", "You Rolled a:","[", die1,"]")
                print("...................................")
                Player += die1 + die2
                print("[", name,"]", "Your total so far is:", "[",Player,"]")
                print("..........................................")                          
            else:
                # Displays results of dice roll
                print("[", name,"]", "You rolled a:", "[",die1,"]", "\nand...............a:","[", die2,"]")
                print()
                Player += die1 + die2
                print("[", name,"]", "Your total so far is:", "[",Player,"]")         
                
        else:
            Player_stay = True
        # Display  House results according to score
        if Player > 21 and House < 22:
            print("BUST! ...", "[", name, "]", "LOST ... House is the WINNER!!!\n")
        elif Player == 21:
            print("Congratulations!", "[", name, "]",  "You made it to 21 ... WINNER !!!\n")
        elif Player < 22 and House > 21:
            print("BUST! ... House LOST ..." ,"[", name, "]", "is the WINNER!\n") 
            print()
            play_again = "y"
            main()
            play_again = input("Do you want to play Vingt-Et-Un again? (y/n) ").lower()
            print("")
        # Display House and Player results if both decide to Stay
        if House_stay and Player_stay:
            if Player > House and Player < 21 and House < 21:
                print("House LOST ...","[", name, "]","is the WINNER !!!\n")    
            elif Player == 21 and House > 21:
                print("BUST! ... House LOST ...","[", name, "]","is the WINNER !!!\n")  
            elif Player > House and House == 21:
                print("BUST! ... ","[",name,"]","LOST ... House is the WINNER !!!\n")
            elif House > Player and House < 21 and Player < 21:
                print("[",name,"]","LOST ... House is the WINNER !!!\n")
            elif Player > 21 and House < 21:
                print("BUST! ...", "[", name, "]", "LOST ... House is the WINNER !!!\n")
            elif Player == 21:
                print("Congratulations!", "[", name, "]", "You made it to 21 ... WINNER !!!\n")    
            elif House == 21 and Player == 21:
                print("Game Over! ... It's a TIE !!!\n")
            elif House == Player:
                print("Game Over! ... It's a TIE !!!\n")
                # Option to play again
                play_again = "n"
main()
                
        

       
    
