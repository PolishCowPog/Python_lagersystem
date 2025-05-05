import json
import os


product_name = "test"
product_price = 100.0

file_empty = True


data = {"Product": product_name, 
        "Price": product_price}

if not os.path.exists('test.json') or os.path.getsize('test.json') == 0:
    print("File is empty!")
    file_empty = True
else:
    print("File contains data!")
    file_empty = False


with open('test.json', 'at') as file:
    if file_empty == False:
        
        file.write(",\n")

    json.dump(data, file)