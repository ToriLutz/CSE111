#Victoria Lutz

#to import the library 
import math
import datetime

#gets current date 
current_date = datetime.date.today()

#this is for pi 
pi = math.pi 
#prompts inputs for equation
width = int(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

   
#calculates the volume 
volume = pi * width**2 * aspect_ratio *(width * aspect_ratio + 2540 * diameter) /10000000000

##to determine price of tire
if diameter >= 14:
    price = '$51.99'
elif diameter == 15:
    price = '$55.99'
elif diameter == 16: 
    price = '$156.99'
elif diameter <= 17:
    price = '$169.99'
    


#prints the answer
print(f'The approximate volume is {volume:.2f} liters')
print(f'Your price if you purchased from us would be {price} per tire') 

#This is to input if a use would like to purchase a tire    
buy = input('Would you like to purchase a tire with dimensions that were entered? (Y/N): ')

if buy.lower() == 'n':
    print('Have a good day')
    quit
elif buy.lower() == 'y':
    number = input('Please insert your phone number so an associate can call you: ')
else:
    print('uh oh looks like you did not input a valid option')
    buy = input('Would you like to purchase a tire with dimensions that were entered? (Y/N): ')
    print('Have a nice day :-)')
    quit
    
    
    
#creates the appended file and puts everything in said file 
with open('volumes.txt', 'a')as f:
    f.write('{}, {}, {}, {}, {}, {} \n' .format(
        current_date, width, aspect_ratio, diameter, round(volume,2), number)
            )