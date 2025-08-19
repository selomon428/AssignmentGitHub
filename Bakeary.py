inventory = {}

# Function to add a new ingredient
def add_ingredient (name, quantity, unit):
    if name not in inventory:
        inventory[name] = {'quantity': quantity, 'unit': unit}
        print(f"{name} added with {quantity} {unit}.")
    else:
        print ("Ingredient already exists.")

#Function to check the current inventory
def check_inventory ():
    print ("\n Inventory:")
    for name, details in inventory.items():
        print(f"{name}: {details['quantity']} {details['unit']}")

#Function to update an ingredient's quantity
def update_ingredient(name, used_amount):
    if name in inventory:
        current_quantity = inventory[name]['quantity']
        if used_amount <= current_quantity:
            inventory[name]['quantity'] -= used_amount
            print(f"{used_amount} {inventory[name]['unit']} of {name} used. Remaining: {inventory[name]['quantity']} {inventory[name]['unit']}")
        else:
            print (f"Not enough {name} in inventory to use {used_amount} {inventory[name]['unit']}.")
    else:
        print(f"{name} not found in inventory.")

# Sample usage
add_ingredient ("Sugar", 500, "grams")
add_ingredient ("Flour", 1000, "grams")
check_inventory ()
update_ingredient ("Sugar", 150)
check_inventory ()

