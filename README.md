# -6-days-Training---Python-for-Aspiring-Data-Scientists-
By fork coding school

# Day 1

# Assignments - 1

"""
Name: 
    Adult Body Mass Index Calculator         
Filename:
    bmi_cal.py
Problem Statement:
    Assuming your weight in kilogram and height in meters  
    Calculate your BMI value and print it ?
    Take the height and weight of the user from input 
Hint: 
    How to caltulate your BMI ?
    Divide your weight in kilograms (kg) by your height in metres (m)
    Then divide the answer by your height again to get your BMI

This would be helpful since you need to convert your own height into meters 
    1 Feet = 0.3048 m
    1 Inch = 0.0254 m
""" 


# Assignments - 2

"""
Name: 
    Ride Cost Calculator         
Filename:
    ridecost_cal.py
Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office.
    Take the distance travelled, cost of diesel and Fuel Average from input 
Hint:    
    fuel_consumption = (travelling_km / vehicle_fuel_avg)
    cost_per_day = (diesel_cost * fuel_consumption)
"""

# Day 2

# Assignments - 3

"""
Name: 
    Clean the Messy salary        
Filename:
    salary.py
Problem Statement:
    Clean the Messy salary into integers for Data Processing
    salary = '$876,001'
    
    Remove the $
    Remove the ,
    Convert the string into integer
Hint: 
    We can use slicing concept to remove $ or replace() method 
    We can use the split and join to remove the , comma
    We can use the int() typecast to convert into integer
"""



# Assignments - 4

"""
Name: 
    Senior Citizen          
Filename:
    ifelse.py
Problem Statement:
    Take the age as input from the user
    print whether he is a infant, Child, Adult,  Senior Citizen
Hint: 
    > 0  and <=1   is Infant
    > 1  and <=18  is Child 
    > 18 and <= 60 is Adult
    > 60 then it   is Senior Citizen
"""


# Assignments - 5

"""
Code Challenge
  Name: 
    Fizz Buzz
  Filename: 
    fizzbuzz.py
  Problem Statement:
    Write a Python program which iterates the integers from 1 to 50(included). 
    For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz". 
    User Input not required  
  Output:
    1
    2
    Fizz
    4 
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
"""

 # Interactive Guess the Number Game 

"""
Challenge 1
    The computer will think of a random number from 1 to 10 as secret number
"""


"""
    Then ask you ( Player ) to guess the number and store as guess number
"""



"""



    Compare the guess number with the secret number 
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

"""
# Day 3

"""
Challenge 1
    We are going to make a "Shopping List" app. 
    Run the script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT the program
    And once i quit, I want the app to show me everything thats on my list.

Hint 1
#pseudocode 
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use the app

    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app with DONE

    Step 6: print out the list
"""


# Assignments - 6

"""
Name: 
    Clean the Messy salary from list        
Filename:
    salary2.py
Problem Statement:
    salaries = ['$876,001', '$543,903', '$2453,896'] 
    Clean the Messy salaries into integers for Data Processing
    Remove the $
    Remove the ,
    Convert into integer
Hint: 
    We can use slicing concept to remove $ or remove() method 
    We can use the split and join to remove the , comma
    We canuse the int() typecast to convert into integer
"""

# Assignments - 7

"""
Name: 
    Shopping List        
Filename:
    shopping.py
Problem Statement:
    We are going to make a "Shopping List" app. 
    Run the python script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT the program
    And once i quit, I want the app to show me everything thats on my list.

Hint:
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use the app

    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app with DONE

    Step 6: print out the list
"""


# Day 4

"""
Challenge 1
    We are going to make a "Shopping List" app. 
    Run the script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT the program
    And once i quit, I want the app to show me everything thats on my list.

Hint 1
#pseudocode 
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use the app

    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app with DONE

    Step 6: print out the list

Challenge 2
    If I type SHOW, 
    I should be able to see what is currently in the list

    If I type HELP, 
    I should be able to see all the help for these special commands

Hint 2
    Step 1: Have a HELP command
    Step 2: Have a SHOW command
    Step 3: Add a function for adding into the list 
    Step 4: Cleanup the code in general

Challenge 3

    There should be a functionality to remove items from the list at a specific index using REMOVE
""" 

# Assignments - 8

"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number    Book Title              Author      Quantity    Price per Item
    34587           Learning Python         Mark Lutz   4           40.95
    98762           Programming Python      Mark Lutz   5           56.80
    77226           Head First Python       Paul Barry  3           32.95
    88112           Einführung in Python3   Bernd Klein 3           24.99    
    
    
    Write a Python program, 
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 

    Output:
    [('34587', 163.8), ('98762', 284.0), ('77226', 98.85), ('88112', 74.97)]
    
    The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.
    
    Output:
    [('34587', 163.8), ('98762', 284.0), ('77226', 108.85), ('88112', 84.97)]
    
    

  Hint: 
    Write a Python program using lambda and map.
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
      ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
      ["77226", "Head First Python, Paul Barry", 3,32.95],
      ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
    ]

"""