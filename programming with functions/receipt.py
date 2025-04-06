##for the extra credit i made a return by date on the receipt using the timedelta function 

import csv
from datetime import datetime,timedelta 



def main():
    
        try:
            ##to find the date today
            current_date_and_time = datetime.now()
            #getting all the lists and dictionaries 
            receipt_lines = make_receipt()
            total = total_price()
            amount = len(total)
            
            total_sum = sum(total)
            tax = total_sum * 0.06 
            final_price = total_sum + tax
            ##using this to find out the date to return the receipt by! 
            future_date = current_date_and_time + timedelta(days=30)
            
            
            print("STORE NAME")
            print(f"{current_date_and_time:%Y-%m-%d}")
            print("\n".join(receipt_lines))
            print(f"amount of items: {amount}")
            print(f"Before Tax ${total_sum}")
            print(f"tax: ${tax:.2f}")
            print(f"Total: ${final_price:.2f}")
            ##return time here 
            print(f"Return by: {future_date:%Y-%m-%d} 9:00PM")
            print("Thank you for shopping at STORE NAME")
        except  FileNotFoundError as not_found_err:
            print()
            print(type(not_found_err).__name__, not_found_err, sep=": ")
            print("This file is not available")
            print("Please run the system again with the proper file")
            print("maybe it's not in the same folder?")
        except PermissionError as perm_err:
            print()
            print(type(perm_err).__name__, perm_err, sep=": ")
            print("Looks like you don't have the permission to do that")
            print('Please run the program again when the correct permissions are in place')
        
        except KeyError as key_err:
            print()
            print(type(key_err).__name__, key_err, sep=": ")
            print("something is wrong please try again")


def make_receipt():

    ##Request.csv
    REQUEST_PRODUCT_INDEX = 0
    QUANTITY_INDEX = 1
    ##Products.csv
    PRODUCT_INDEX = 0
    PRICE_INDEX = 2
    
    ##This is to READ PRODUCT DICTIONARIES 
    product_dict = read_dictionary("products.csv", PRODUCT_INDEX)
    
    receipt_lines = [] 
    
    
    #To read and go through the request list so we can compare them to the PRODUCTS list
    with open ("request.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            product_num = row_list[REQUEST_PRODUCT_INDEX]
            product_quantity = row_list[QUANTITY_INDEX]
            
            if product_num in product_dict and len(row_list) != 0:
                product_info = product_dict[product_num]
                price_amount = float(product_info[PRICE_INDEX])
                total_price = int(product_quantity) * float(price_amount)
                receipt_lines.append(f'Product: {product_info[1]}, Quantity: {product_quantity},  ${total_price:.2f}') 
               
                
                
                
    return receipt_lines
    
 
def total_price():
    
    ##Request.csv
    REQUEST_PRODUCT_INDEX = 0
    QUANTITY_INDEX = 1
    ##Products.csv
    PRODUCT_INDEX = 0
    PRICE_INDEX = 2
    
    product_dict = read_dictionary("products.csv", PRODUCT_INDEX)
    total_prices = []
    
    with open ("request.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            product_num = row_list[REQUEST_PRODUCT_INDEX]
            product_quantity = int(row_list[QUANTITY_INDEX])
            if product_num in product_dict and len(row_list) != 0:
                product_info = product_dict[product_num]
                price_amount = float(product_info[PRICE_INDEX])
                total_price_for_item = price_amount * product_quantity
                total_prices.append (total_price_for_item)
    return total_prices
                


def read_dictionary(filename, key_column_index):
  """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.
  Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
  Return: a compound dictionary that contains
      the contents of the CSV file.
  """
  dictionary = {}
    
  with open(filename, mode="rt") as csv_file:
        reader = csv.reader(csv_file) 
        
        next(reader)  
        for row_list in reader:
            if len(row_list) != 0: 
                key = row_list[key_column_index]
                dictionary[key] = row_list  
            
  return dictionary 
  
if __name__ == "__main__":
    main()

 