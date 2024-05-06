def greet():
    print("\nHello I am a chatbot for Gaco Bell. How can I help you ?")
    options = """ 1] Browse menu. \n 2] Order a takeout. \n 3] Book a table. \n 4] Exit"""
    print(options)

def greet_1():
    print("\nWhat else ?")
    options = """\n 1] Browse menu. \n 2] Order a takeout. \n 3] Book a table. \n 4] Exit"""
    print(options)

def menu():
    menu = """\nSNACK \n 1] Pohe \n 2] Vadapav \n 3] Pattice \n\n LUNCH \n 1] Vegthali
 2] Chickenthali \n 3] Andathali \n\n  DRINKS \n 1] Soda \n 2] Cocktail"""
    print(menu)

def order():
    menu = ["pohe", "vadapav", "pattice", "vegthali", "chickenthali", "andathali", "soda", "cocktail"]
    print("\nWhat would you like to order ?")
    while(True):
        item = input().lower()
        if(item not in menu):
            print("Sorry. We do not serve this item. Choose another item.")
        else:
            break
    number = int(input("how many ? \n"))
    address = input("enter address : ")
    name = input("enter name : ")
    order = {"item" : item, "number": number, "name":name, "address": address}
    print("here is the summary.")
    print(order)

def book():
    date = input("Enter the date.")
    print("Time for booking ?")
    time = input()
    number = int(input("how many people ? \n"))
    name = input("enter name : ")
    booking = {"name":name, "number": number, "date": date, "time": time}
    print("here is the summary.")
    print(booking)


def end():
    print('Goodbye, have a nice day!')
    print('.................................')
    print('.................................')
    quit()

greet()    
while(True):
    option = input()
    if(option == "1" or option == "Browse menu"):
        menu()
    elif(option == "2" or option == "Order a takeout"):
        order()
    elif(option == "3" or option == "Book a table"):
        book()
    elif(option == "4" or option == "Exit"):
        end()
        break
    else:
        print("Please enter a valid choice.")
    greet_1()