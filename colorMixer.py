inputcolor1 = input('Enter primary color:').lower()
inputcolor2 = input('Enter primary color:').lower()
if (inputcolor1 == 'red' and inputcolor2 == 'blue') or \
   (inputcolor1 == 'blue' and inputcolor2 == 'red'):
    print('When you mix red and blue, you get purple.')
elif (inputcolor1 == 'red' and inputcolor2 == 'yellow') or \
     (inputcolor1 == 'yellow' and inputcolor2 == 'red'):
    print('When you mix yellow and red, you get orange.')
elif (inputcolor1 == 'blue' and inputcolor2 == 'yellow') or \
     (inputcolor1 == 'yellow' and inputcolor2 == 'blue'):
    print('When you mix blue and yellow, you get green.')
elif (inputcolor1 != 'blue' and inputcolor1 != 'red' and inputcolor1 != 'yellow'):
    print('You didn'"'"'t input two primary colors.')
elif (inputcolor2 != 'blue' and inputcolor2 != 'red' and inputcolor2 != 'yellow'):
    print('You didn'"'"'t input two primary colors.')
