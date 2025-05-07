import json
import os


# IMAGES ------------------------------------------------------------------------------------------------

def print_logo():
    logo = """

                    __          _                               ____  ____       __                   
  _____ _____ _____| _|     ___| |_ ___  _ __ ___              |  _ \| __ )     |_ |_____ _____ _____ 
 |_____|_____|_____| |     / __| __/ _ \| '__/ _ \    _____    | | | |  _ \      | |_____|_____|_____|
 |_____|_____|_____| |     \__ \ || (_) | | |  __/   |_____|   | |_| | |_) |     | |_____|_____|_____|
                   | |     |___/\__\___/|_|  \___|             |____/|____/      | |                  
                   |__|                                                         |__|                  

    """
    print(logo)

def print_add_product():
    logo = """

                    __         _       _     _      ____                _            _        __                   
  _____ _____ _____| _|       / \   __| | __| |    |  _ \ _ __ ___   __| |_   _  ___| |_     |_ |_____ _____ _____ 
 |_____|_____|_____| |       / _ \ / _` |/ _` |    | |_) | '__/ _ \ / _` | | | |/ __| __|     | |_____|_____|_____|
 |_____|_____|_____| |      / ___ \ (_| | (_| |    |  __/| | | (_) | (_| | |_| | (__| |_      | |_____|_____|_____|
                   | |     /_/   \_\__,_|\__,_|    |_|   |_|  \___/ \__,_|\__,_|\___|\__|     | |                  
                   |__|                                                                      |__|                  

    """
    print(logo)


# ADD PRODUCT ------------------------------------------------------------------------------------------------
product_name = "null"
product_price = 0.0
product_category = "null"
product_amount = 0


def add_product_menu():
    print(f"Product Name: {product_name}")
    print(f"Product Price: {product_price}")
    print(f"Product Category: {product_category}")
    print(f"Product Amount: {product_amount}")
    print("")
    print("Chanege values(1-4):")
    print("1. Product Name")
    print("2. Product Price")
    print("3. Product Category")
    print("4. Product Amount")
    print("")
    print("5. Confirm and add product")
    print("6. Cancel and return to main menu")
    print("")
    print("")



def add_product():

    os.system('cls')

    print_add_product()

    add_product_menu()

    choice = input("Enter your choice (1-4 / 5-6): ")
    


    file_empty = True


    data = {"Product": product_name, 
            "Price": product_price,
            "Category": product_category,
            "Amount": product_amount}

    if not os.path.exists('test.json') or os.path.getsize('test.json') == 0:
        print("File is empty!")
        file_empty = True
    else:
        print("File contains data!")
        file_empty = False

    with open('test.json', 'rb+') as file:
        if file_empty == False:
            file.seek(-2, os.SEEK_END)
            file.truncate()

    with open('test.json', 'at') as file:
        if file_empty == False:
            file.write(",\n")
        if file_empty == True:
            file.write("[\n")
        json.dump(data, file, indent=2)
        file.write("\n]")

#remove()
#write()

# FIND PRODUCT ------------------------------------------------------------------------------------------------

def read_product(product_name):
    with open('test.json', 'r') as file:
        data = json.load(file)
        for product in data:
            if product["Product"] == product_name:
                return product
    return None

# Example usage:
product = read_product("test2")
if product:
    print(f"Found product: {product}")
else:
    print("Product not found")



# MAIN MENU ------------------------------------------------------------------------------------------------
def main_menu():

    print_logo()

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_product()
    else:
        os.system('cls')
        main_menu()



# RUN PROGRAM --------------------------------------------------------------------------------------------
os.system('cls')
main_menu()