import json
import os
from colorama import Fore, Style

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
    print(Fore.GREEN + logo + Fore.WHITE)

def print_add_product():
    logo = """

                    __         _       _     _      ____                _            _        __                   
  _____ _____ _____| _|       / \   __| | __| |    |  _ \ _ __ ___   __| |_   _  ___| |_     |_ |_____ _____ _____ 
 |_____|_____|_____| |       / _ \ / _` |/ _` |    | |_) | '__/ _ \ / _` | | | |/ __| __|     | |_____|_____|_____|
 |_____|_____|_____| |      / ___ \ (_| | (_| |    |  __/| | | (_) | (_| | |_| | (__| |_      | |_____|_____|_____|
                   | |     /_/   \_\__,_|\__,_|    |_|   |_|  \___/ \__,_|\__,_|\___|\__|     | |                  
                   |__|                                                                      |__|                  

    """
    print(Fore.GREEN + logo + Fore.WHITE)

def print_find_product():
    logo = """

                       ___   ______ _           _                         _            _  ___                      
  ______ ______ ______|  _| |  ____(_)         | |                       | |          | ||_  |______ ______ ______ 
 |______|______|______| |   | |__   _ _ __   __| |    _ __  _ __ ___   __| |_   _  ___| |_ | |______|______|______|
  ______ ______ ______| |   |  __| | | '_ \ / _` |   | '_ \| '__/ _ \ / _` | | | |/ __| __|| |______ ______ ______ 
 |______|______|______| |   | |    | | | | | (_| |   | |_) | | | (_) | (_| | |_| | (__| |_ | |______|______|______|
                      | |_  |_|    |_|_| |_|\__,_|   | .__/|_|  \___/ \__,_|\__,_|\___|\__|| |                     
                      |___|                          | |                                 |___|                     
                                                     |_|                                                           

    """
    print(Fore.GREEN + logo + Fore.WHITE)

def print_delete_product():
    logo = """

                       ___   _____       _      _         ___                      
  ______ ______ ______|  _| |  __ \     | |    | |       |_  |______ ______ ______ 
 |______|______|______| |   | |  | | ___| | ___| |_ ___    | |______|______|______|
  ______ ______ ______| |   | |  | |/ _ \ |/ _ \ __/ _ \   | |______ ______ ______ 
 |______|______|______| |   | |__| |  __/ |  __/ ||  __/   | |______|______|______|
                      | |_  |_____/ \___|_|\___|\__\___|  _| |                     
                      |___|                              |___|                     
                                                                                   
    """
    print(Fore.GREEN + logo + Fore.WHITE)

# ADD PRODUCT ------------------------------------------------------------------------------------------------
product_name = "null"
product_price = 0.0
product_category = "null"
product_amount = 0


def add_product_menu():
    print("The currect product will be added with the following values:")
    print(f"Product Name: {product_name}")
    print(f"Product Price: {product_price}")
    print(f"Product Category: {product_category}")
    print(f"Product Amount: {product_amount}")
    print("")
    print("----------------------")
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
    if choice == "1":
        global product_name
        product_name = input("Enter product name: ")
        add_product()
    elif choice == "2":
        global product_price
        product_price = float(input("Enter product price: "))
        add_product()
    elif choice == "3":
        global product_category
        product_category = input("Enter product category: ")
        add_product()
    elif choice == "4":
        global product_amount
        product_amount = int(input("Enter product amount: "))
        add_product()
    elif choice == "5":
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
    elif choice == "6":
        main_menu()
    else:
        add_product()


        



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

def all_products():
    os.system('cls')
    with open('test.json', 'r') as file:
        data = json.load(file)
        for product in data:
            print(f"Product: {product['Product']}   |    Price: {product['Price']}  |    Category: {product['Category']}    |    Amount: {product['Amount']}")

def find_product():
    os.system('cls')
    print_find_product()
    print("1. Search by product name")
    print("2. Show all products")
    print("3. Go back to main menu")

    choice = input("(1-3): ")
    if choice == "1":
        search = input("Enter the name of the product you want to find: ")
        product = read_product(search)
        print(f"Found product: {product}")
    elif choice == "2":
        all_products()
    elif choice == "3":
        main_menu()
    else:
        find_product()

    wait = input("Press enter to continue...")
    main_menu()



# DELETE PRODUCT --------------------------------------------------------------------------------------------
def delete_product(product_name):
    with open('test.json', 'r') as file:
        data = json.load(file)
    
    # Filter out the product with matching name
    updated_data = [product for product in data if product["Product"] != product_name]
    
    # Write the filtered data back to the file
    with open('test.json', 'w') as file:
        json.dump(updated_data, file, indent=2)
        
    print(f"Product '{product_name}' has been deleted.")

# Example usage:

def delete_product_menu():
    os.system('cls')
    print_delete_product()
    delete_product(input("Enter the name of the product you want to delete: "))

# MAIN MENU ------------------------------------------------------------------------------------------------
def main_menu():

    os.system('cls')

    print_logo()
    print("1. Add product")
    print("2. Find product")
    print("3. Delete product")
    print("")
    print("4. Exit")
    print("")

    choice = input("Enter your choice (1-3) (4): ")

    if choice == "1":
        add_product()
    elif choice == "2":
        find_product()
    elif choice == "3":
        delete_product_menu()
    elif choice == "4":
        print("Exiting...")
        exit()
    else:
        os.system('cls')
        main_menu()



# RUN PROGRAM --------------------------------------------------------------------------------------------
print(Fore.WHITE)
print(Style.BRIGHT)
main_menu()