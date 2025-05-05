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

def remove():
    with open('test.json', 'rb+') as file:
        if file_empty == False:
            file.seek(-2, os.SEEK_END)
            file.truncate()

def write():
    with open('test.json', 'at') as file:
        if file_empty == False:
            file.write(",\n")
        if file_empty == True:
            file.write("[\n")
        json.dump(data, file, indent=2)
        file.write("\n]")

#remove()
#write()

def read_product(product_name):
    with open('test.json', 'r') as file:
        data = json.load(file)
        for product in data:
            if product["Product"] == product_name:
                return product
    return None

# Example usage:
product = read_product("test1")
if product:
    print(f"Found product: {product}")
else:
    print("Product not found")