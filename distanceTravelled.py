#DistanceTravelled.py
#Oct 10, 2021
#This program prompts the user for the speed travelled.  A chart is then generated and displayed
#to show the distance travelled for 5 hours

def main():
    #Declare variables
    #float rate, distance
    rate = distance = 0.0
    #int hours
    hours = 0
    #Prompt for rate and validate that the rate is positive
    rate = -1
    while rate < 0:
        rate = float(input("Enter the speed (mph):  "))
        if rate < 0:
            print("Invalid.  Rate must be positive.")
    #Display chart heading
    print("Hours Travelled\tDistance Travelled")
    print("--------------------------------------------------")
    #For loop to create the values in the chart
    for hours in range(1,6):
        #Calculate distance
        distance = hours * rate
       #Display hours   distance
        print(hours, "\t\t", distance)
