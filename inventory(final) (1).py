from tabulate import tabulate  
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
# Now I will create a data list that I will use to to insert all the data about the shoes so I can then print them out 
# later in the view_all function 
data = [["Country", "Code", "Product", "Cost", "Quantity"]]
def read_shoes_data(): 
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
# Now we'll read our data from the inventory text and print an error if the text is not found
path = 'inventory.txt'
file = None
path = 'inventory(final).txt'

try:
    file =  open(path, "r+") 
    next(file)
    for lines in file:
        temp = lines.strip()
        temp = temp.split(",")
        
        data.append(temp)
        shoe_list.append(Shoe(temp[0], temp[1], temp[2], int(temp[3]), int(temp[4])))
except FileNotFoundError:
    print("Unfortunately the file that you are trying to open does not exist")
    
finally:
    if file is not None:
        file.close()
    
def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    country, code, product, cost, quantity = input('''Please enter the following infomation about the show in the following order seperated by a comma and a space(", "):
    -Country
    -Code
    -Product
    -Cost 
    -Quantity
      ''').split(", ")
    temp_list = [country, code, product, cost, quantity]
    data.append(temp_list)
    new_shoe = Shoe(country, code, product, cost, int(quantity))
    shoe_list.append(new_shoe)

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    print(tabulate(data, headers="firstrow", tablefmt="fancy_grid"))    
    
def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # We are going to create an empty list that will be used to store the quantity of all the shoes
    # Then we are are going to find the lowest number in this list and find the show shoe corresponding to this number
    # and ask the user if they would like to add to the quantity of this shoe and update it accordingly 
    temp = []
    for shoe in shoe_list:
        temp.append(shoe.quantity)
    lowest_quantity = min(temp)

     
    for shoe in shoe_list: 
        if lowest_quantity == shoe.quantity:
            print(f"The show with the lowest quantity in stock right now is {shoe.product} with {shoe.quantity} shoes left in stock")
            answer = input("Would you like to add more of these shoes in stock (yes/no): ").lower()
            if answer == "yes":
                add_shoe_amount = int(input(f"How much of the {shoe.product} would you like to add? "))
                new_stock_amount = shoe.quantity + add_shoe_amount
                with open(path, 'w+') as file:
                    contents = file.read()
                    contents = contents.replace(str(shoe.quantity), str(new_stock_amount))
                shoe.quantity = new_stock_amount
                
def seach_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    search_shoe_code = input("Please enter the code of the shoe you are looking for: ")
    # We will look through our list to look for the show and print the details if we find it
    # If we dont find the show we will print an error message
    for shoe in shoe_list:
        if search_shoe_code == shoe.code:
            print(f"These are the details of the shoe that you are looking for {shoe.country}, {shoe.product}, {shoe.cost}, {shoe.quantity}")
            break
    else:
        print("Unfortunately the shoe that you are looking for is not registered in our database")

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    for shoe in shoe_list:
        value = shoe.cost*shoe.quantity
        print(f"The value of the {shoe.product} is R{value}")

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    temp = []
    for shoe in shoe_list:
        temp.append(shoe.quantity)
    highest_quant = max(temp)
    
    for shoe in shoe_list:
        if highest_quant == shoe.quantity:
            print(f"The {shoe.product} is for sale")     

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
# Read the data from our inventory file
read_shoes_data()
while True:
    # Give the user a list of options as to what exactly they can do in the program
    choice = int(input('''Welcome to the Stockhandler 3000! Glad to see you again and what would you like to do this time?
                       
        1.Capture new shoes for the inventory
        2.View all the shoes currently in stock
        3.Restock a particular item
        4.Search a shoe to find its details
        5.Find out the value per shoe 
        6.Find out which shoe is selling the worst and put it up for sale
        7.End program
                       
        So what will we be doing today? (Enter the number): '''))
    # Now execute each option that the user then asks for 
    
    if choice == 1:
        capture_shoes()
        
    elif choice == 2:
        view_all()
    
    elif choice == 3:
        re_stock()
        
    elif choice == 4:
        seach_shoe()
        
    elif choice == 5:
        value_per_item()
    
    elif choice == 6:
        highest_qty()
        
    elif choice == 7:
        print("Till the next time! Hope to see you soon...")
        break