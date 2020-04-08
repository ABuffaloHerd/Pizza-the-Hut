#You can't outpizza the hut v0.9
from commonlib import validate_int, validate_str, TrueFalse
from datetime import datetime

class detailContainer:
    def __init__(self):
        self.phone    = 0
        self.house    = ''
        self.street   = ''
        self.suburb   = ''

    def reset(self):
        self.phone    = 0
        self.house    = ''
        self.street   = ''
        self.suburb   = ''

class Container:
    def __init__(self):
        self.name = ''
        self.cart = []
        self.isDelivery = False

    def reset(self):
        self.name = ''
        self.cart = []
        self.isDelivery = False

details = detailContainer()
container = Container()

pizzaDict = {}
with open("pizza.txt") as f:
    for line in f:
        (key, val) = line.split('||') #String is split at the '||' in the file
        pizzaDict[key] = float(val) #Loads the name as a key, and the price as the value


#Load the names of the pizzas into a list so that the names and values can be accessed as needed
PIZZAKEYS = list(pizzaDict.keys())
DELIVERYFEE = 3.00

def main():
    container.name = validate_str("Please input customer's name: ").title()

    print("Please pick a number to choose an item from the menu below")
    print("-"*30)

    for (key, val), x in zip(pizzaDict.items(), range(len(pizzaDict))):
        print("{} - {}: {:.2f}".format(x, key, val))
    
    while len(container.cart) < 5: #Automatically breaks at 5 items
        choice = validate_int("Enter your number: ", len(pizzaDict) - 1, 0)
        container.cart.append(PIZZAKEYS[choice])

        if not TrueFalse("Would you like to add more items? (Max 5) Y/N "): #Check if user wants to add more items
            break

    printLog(confirmOrder(), True)

def confirmOrder():
    '''
    Prints final order and calculates total cost.
    Also asks if order is pickup or delivery
    Returns total cost
    '''
    cost = 0
    print("-"*20)
    #Is the order to be delivered?
    container.isDelivery = TrueFalse("Is this order for delivery? Y/N ")
    if container.isDelivery:
        cost += DELIVERYFEE
        print("_"*20)
        getDetails()

    else:
        print("_"*20)

    #Print the order
    print("ORDER FOR: {}".format(container.name))
    print("~"*10)
    for x in range(len(container.cart)):
        print("{} - ${:.2f}".format(container.cart[x], pizzaDict.get(container.cart[x])))
        cost += pizzaDict.get(container.cart[x]) #Add to the total cost

    if container.isDelivery: #Include the delivery fee in the reciept
        print("DELIVERY FEE - ${:.2f}".format(DELIVERYFEE))

    print("TOTAL: {:.2f}".format(cost))
    if container.isDelivery: #If it is for delivery, print the customer's details
        print("-"*10)
        print("{} {} {}\nPH: {}". format(details.house, details.street, details.suburb, details.phone))


    if not TrueFalse("Please confirm the order and input Y to proceed, or N to cancel, Y/N "):
        printLog(cost, False)
        reset()

    return cost

def getDetails():
    ''' Collects customer details and adds them to the detail container
        Returns nothing
    '''
    confirm = False
    while not confirm:
        details.phone = validate_int("Please enter customer's phone number: ")
        details.house = input("Please enter customer's house number: ")
        details.street = validate_str("Please input customer's street: ")
        details.suburb = validate_str("Please input customer's suburb: ")

        confirm = TrueFalse("Enter Y to confirm or N to start over. Y/N ")
    print("_"*20)

def printLog(cost, completed):
    '''
    Prints an audit log
    Takes cost as a parameter because that is not stored in any public class
    Takes completed as a parameter because that is also not stored in any class
    '''
    
    now = datetime.now()
    with open("log.txt", "a") as y:
        y.write("\n")
        y.write("Time: {}; "
                "Is delivery?: {}; "
                "Customer: {}; "
                "Number pizzas ordered: {}; "
                "Total: {}; ".format(now, container.isDelivery, container.name.title(), len(container.cart), cost))
        y.write("Completed: {};".format(completed))

def reset():
    '''Does exactly what it's called'''
    #Reset classes
    container.reset()
    details.reset()
    main() #Restart

main()
