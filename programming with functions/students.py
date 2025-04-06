import csv

def main():
    NAME_INDEX = 1  # Assuming the name is in the first column
    name_dict = read_dictionary("students.csv", NAME_INDEX)
    print(name_dict)

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.
    
    Parameters
        filename: the name of the CSV file to read.
        
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    
    dictionary = {}
  
    with open(filename, mode="rt") as csv_file:
        reader = csv.reader(csv_file)  
        
        next(reader)  # Skip header if there is one
        for row_list in reader:
            if len(row_list) != 0:  # Check if the row is not empty
                key = row_list[key_column_index]
                dictionary[key] = row_list  # Store the entire row as a list
            
    return dictionary 

if __name__ == "__main__":
    main()