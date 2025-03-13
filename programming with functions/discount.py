##victoria lutz 

##import library 
from datetime import datetime

#this calls the current date from datetime library 
current_date = datetime.now()
day_of_week = current_date.weekday()

sales_tax = 0.06

subtotal = float(input('Please input your subtotal: '))

discount = round(subtotal *.1) 
tax = round(subtotal * sales_tax , 2)

discount_total = (subtotal + tax)-discount
total = subtotal + tax

if subtotal >= 50 and day_of_week == (1 or 2):
    print(f'subtotal: {subtotal:.2f}')
    print(f'sales tax: {tax:.2f}')
    print(f'discount amount: {discount:.2f}')
    print(f'your total is {discount_total:.2f}')
else:
    print(f'your subtotal is: {subtotal}')
    print(f'your sales tax is: {tax}')
    print(f'your total is {total:.2f}')