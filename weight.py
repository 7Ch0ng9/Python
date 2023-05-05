# weight.py
# David Chong
# October 8,2021
# Weight Loss Pal. This menu-driven program states that if a moderately active
# person cuts their calorie intake by 500 calories a day, they can typically
# loose 4 pounds a month. The program promts the user to select from 3 options that can help with
# weight loss. 
# Algorithm:
# For option 1, the following guidelines will be displayed:
# Try these 10 ways to cut 500 calories every day.
# Swap your snack.
# Cut one high-calorie treat.
# DO NOT drink your calories.
# Skip seconds.
# Make low calories substitutions.
# Ask for a doggie bag.
# Just say "no" to fried food.
# Build a thinner pizza.
# Use a smaller plate
# Avoid alcohol.
# For option 2, the program will prompt the user for the starting weight which cannot be less than
# 100 pounds. The program will generate a table showing what the expected weight will be at the
# end of each month, for the next six months after starting the following guidelines. 
# For option 3, the program will end.

def main():
    
        option = 0

        while option != "3":
                                
                # Display Intro
                # Prompts user to select an option
                print()
                print("500 Less a Day Makes The Weight Go Away...")
                print()
                print("Choose one of the options:")
                print("        1. Display ""10 ways to cut 500 calories"" guidelines.")
                print("        2. Generate next semester expected weight table.")
                print("        3. Quit")
                print()
                option = input()

                if option == "1":
                        print("Option: 1")
                        print()
                        print("Try these 10 ways to cut 500 calories every day.")
                        print("         * Swap your snack.")
                        print("         * Cut one high-calorie treat.")
                        print("         * Do NOT drink your calories.")
                        print("         * Skip seconds.")
                        print("         * Make low calorie substitutions.")
                        print("         * Ask for a doggie bag.")
                        print("         * Just say ""no"" to fried food.")
                        print("         * Build a thinner pizza.")
                        print("         * Use a smaller plate")
                        print("         * Avoid alcohol")
                        print("Source: US National Library of Medicine")
                        

                elif option == "2":
                        print("Option: 2")
                        # Declare variables
                        Weightloss = 4
                        Month = 0
                        Current_weight = 0
                        # Promt user for weight
                        Month = Month + 1
                        Current_weight = Current_weight + 1
                        while Current_weight <100:
                            Current_weight = int(input("Please enter starting weight in pounds: (>=100) "))
                            if Current_weight <100:
                                    print("     Error ... Invalid weight. Try Again")
                                    print()
                                    while Current_weight >=100:
                                        Current_weight = int(input("Please enter starting weight in pounds: (>=100)"))
                                        Weightloss = 4
                        for Month in range(6):
                                Current_weight -= Weightloss
                                # Display chart heading
                                print()
                                print("Month:{}\tWeight:{}".format(Month + 1, Current_weight))
                                print("----------------")
                                         
         
                elif option == "3":
                        print("Option: 3")
                        print()
                        print("Good Bye...")

                else:
                        print("Error ... Invalid option. Try Again")
        


