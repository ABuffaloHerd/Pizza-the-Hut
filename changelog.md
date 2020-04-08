24/03/2020
Restarted

TODO for V1.0
Create classes for stack and container DONE
Main function to get customer details DONE
Main function to print menu and keep track of orders (up to 5) DONE
Main function to confirm orders DONE

Additional function to calculate total cost DONE
Additional function to ask if delivery and add delivery fee DONE
Additional function to collect customer address and phone DONE

Main function to print final order with total cost
Additional function to print to audit log

VALIDATION to be added via commonlib.py
PIZZAS to be stored in dictionary
PIZZA names to be stored as a list to make dictionary access easier

NICE TO HAVES
A menu of sides V1.1
Pizzas and prices are already in one text file V1.0
Comments can be added to pizza file and are denoted C-style ('//') V1.2

V0.1a 24/03
 + Created classes for stack and container

    Stack
        Attributes
            list    items

        Methods
            none    Push 
            element Pop
            bool    isEmpty
            element Peek
    
    Container 
        Attributes
            str             name
            list(string)    cart
            list(float)     prices
            bool            isDelivery

Declared constant for delivery fee

TEST
Program returns no error on run

v0.2a
+ Added read functionality to create a dictionary from a text file that contains both pizza names and prices
~ Declared two stacks
~ Declared one container
~ Declared one dictionary
+ Printed dictionary after read function

TEST
Program returned no error on run

v0.3a
- Removed debug print for dictionary
Main function to print dictionary elements
Main function get input from user and load into container.cart

Added method to Container that automatically takes the price of a pizza and loads it into the prices list

    Container
        Methods
            none    addPizza

Added constant list of pizza names created from dictionary

TEST

RUN
    NameError: name 'pizzaDict' is not defined
        FIX V0.3b: 
            Moved declaration of PIZZALIST to after pizzaDict is loaded
            For sake of tidiness moved declaration of DELIVERYFEE to line below

32 into input at menu
    IndexError: list index out of range

'meow' into input at menu
    ValueError: invalid literal for int() with base 10: 'meow' 


FIX: V0.4a
Imported commonlib to deal with errors
Refer to commonlib changelogs for information on any changes

V0.5a
- Removed stack because apparently you don't need it.
+ Replaced it with a class that holds information on the customer (Address etc..)

    detailContainer
        Attributes
            int phone
            str house
            str street
            str suburb
            int postcode

- Removed addPizza method from Container
    The calculation function will use the names to calculate the total cost using the dictionary, instead of another list

+ Added loop that checks if there are more than 5 items in the cart

V0.5b
+ Added option to stop adding items to cart after each item is added.
+ Prettified questions and spacing

V0.6a
+ NEW confirmOrder function to confirm the order and to calculate the total cost.
    Asks if the order is for pickup or delivery
    If delivery, run additional function that collects the address etc. 

V0.7
+ NEW getDetails function to acually utilize the detailContainer object and collect customer details
~ Moved printing of obnoxious "ORDER FOR DELIVERY"
- If order is for delivery, then details are collected before the program prints the final order
    If the order is for pickup only, then the details are not printed

+ Added input for customer's name
+ The receipt printing now also lists the delivery fee if needed

V0.8
+ Final features to be added
+ NEW Now prints an audit log from container classes.
    + Added import datetime
+ NEW method for both classes: reset. Does exactly what it's called
+ Fixed typo with detail container. How and why it still ran will forever continue to bamboozle me
- Removed unused variable totalCost
- Cleaned up debug commands

V0.9 beta1
+ NEW Reset function that just resets and restarts everything to save on code
+ Tidied code
    - Removed unused imports
+ Tidied reciept printing
    - Removed postcode
    - Removed more debug printing