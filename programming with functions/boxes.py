##victoria lutz 
##importing math 
import math
#functions 
items = int(input('Enter number of items: '))
boxes = int(input('Enter the number of items per box: '))


answer = math.ceil(items/boxes)
print(f'for {items} items with {boxes} items per box you will need {answer} boxes')