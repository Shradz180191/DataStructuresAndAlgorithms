'''
Create a “Fantasy Game Inventory” using a dictionary

You are creating a fantasy video game.  The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value of how many of that item the player has. For example,  {‘gold’: 1, ‘mana potions’: 3, ‘healing potion’: 6, ‘arrow’: 12, ‘dagger’: 1, ‘sword’: 3}.  This means the player has 1 gold, 3 mana potions, 6 healing potions,  12 arrows, 1 dagger and 3 sword.

 

Write a function named displayInventory() that would take any possible inventory and display it like the following:

Inventory:

7 gold

3 mana potions

6 healing potions

15 arrow

1 dagger

3 sword

Total number of Items: 26

 

When you loot something you want to add that information to your inventory.

Define a sperate function, add_to_Inventory() that will open an loot variable and add it to the inventory.

Troll Cave loot is 2 gold coins, 1 torch, 1 helm, 1 elven sword

You can use the for loop to loop through all of the keys in the dictionary

Your program should call the function from the main function
'''

inventory = {'gold': 1
                , 'mana potions': 3
                , 'healing potion': 6
                , 'arrow': 12
                , 'dagger': 1
                , 'sword': 3
            }

def displayInventory(inventory):
    '''
        description: display items and number of items in an inventory
        input: dictionary of inventory
        output: prints the list and count of items
    '''
    count = 0

    if len(inventory) == 0:
        print('\nInventory is Empty!!')

    else:
        for i in inventory:
            print(inventory[i],' ',i)
            count = count + inventory[i]

    print('\nTotal number of items: ',count)


def add_to_inventory(inventory=None):
    '''
        description: add item and count to the inventory
        input: inventory
        output: item added to the inventory
    '''
    item = input('\nName of item: \t')
    n = int(input('\nCount of item: \t'))
    if inventory == None:
        inventory = {}
    
    inventory[item] = n
    return inventory

def menu():
    print('\n1. Display Inventory')
    print('\n2. Add to inventory')
    c = int(input('\n\tEnter you choice (1/2):\t'))
    if c not in (1,2):
        print('\n Invalid choice!')
        menu()
    else:
        return c

def main():

    inventory = {}
    choice = 'y'
    while(choice == 'y'):
        c = menu()
        if c == 1:
            displayInventory(inventory)
            choice = input('\nContinue (y/n):\t')
        elif c == 2:
            inventory = add_to_inventory()
            choice = input('\nContinue (y/n):\t')
        else:
            break

main()
