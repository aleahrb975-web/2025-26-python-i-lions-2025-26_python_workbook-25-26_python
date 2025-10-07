"""
Exercise 34:  Even or Odd?
Write a program that reads an integer from the user.  
Then your program should display a message indicating whether
the integer is even or odd    
"""
def even_odd():
    num = int(input("enter a number: "))
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")
        
#even_odd()



"""
Exercise 36:  Vowel or consonant
In this exercise you will create a program that reads a letter
of the alphabet from the user.  If the user enters a, e, i, o, or u
then your program should display a message indicating that the 
entered letter is a vowel.  If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and 
sometimes y is a consonant.  Otherwise your program should display
a message indicating that the letter is a consonant.
"""
def vowel_consonant():
    letter = input("enter a letter: ").lower()
    if letter in 'aeiou':
        print(f"{letter} is a vowel")
    elif letter == 'y':
        print(f"{letter} is sometimes a vowel, sometimes a consonant")
    else:
        print(f"{letter} is a consonant")
        
#vowel_consonant()
"""
Exercise 40:  Name that triangle
A triangle can be classified based on the lengths of its sides as
equilateral, isosceles, or scalene.  All 3 sides of an equilateral
triangle have the same length.  As isosceles triangle has two sides
that are the same length, and a third side that is a different length.
If all of the sides have different lengths then the triangle is scalene.

Write a program that reads the lengths of 3 sides of a triangle from the
user.  Display a message indicating the type of triangle

******  CHALLENGE:
Perform the same task as above but with angles and not sides.
"""
def name_that_triangle():
    side1 = float(input("enter length of side 1: "))
    side2 = float(input("enter length of side 2: "))
    side3 = float(input("enter length of side 3: "))
    
    if side1 == side2 == side3:
        print("the triangle is equilateral")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("the triangle is isosceles")
    else:
        print("the triangle is scalene")
def name_that_triangle_challenge():
    angle1 = float(input("enter angle 1: "))
    angle2 = float(input("enter angle 2: "))
    angle3 = float(input("enter angle 3: "))
    
    if angle1 == angle2 == angle3:
        print("the triangle is equilateral")
    elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
        print("the triangle is isosceles")
    else:
        print("the triangle is scalene")
        
#name_that_triangle()
#name_that_triangle_challenge()
"""
Exercise 55: Cell Phone Bill
A particular cell phone plan includes 50 minutes of air time and
50 text messages for $15.00 a month.  Each additional minute of 
air time costs $0.25 , while additional text messages cost $0.15
each.  All cell phone bills include an additional charge of $0.44
to support 911 call centers, and teh entire bill (including the 
911 charge) is subject to a 5 percent sales tax.

Write a program that reads the number of minutes and text messages
used in a month from the user.  Display the base charge, additional
minutes charge (if any), additional text message charge (if any), 
the 911 fee, tax and total bill amount.  Only display the additional 
minute and text charges if the user incurred costs in these 
categories.  Ensure that all of the charges are displayed using 2
decimal points
"""
def cell_phone_bill():
    base_charge = 15.00
    additional_minute_charge = 0.25
    additional_text_charge = 0.15
    fee_911 = 0.44
    tax_rate = 0.05
    
    minutes = int(input("enter number of minutes used: "))
    texts = int(input("enter number of text messages used: "))
    
    additional_minutes = max(0, minutes - 50)
    additional_texts = max(0, texts - 50)
    
    additional_minutes_cost = additional_minutes * additional_minute_charge
    additional_texts_cost = additional_texts * additional_text_charge
    
    subtotal = base_charge + additional_minutes_cost + additional_texts_cost + fee_911
    tax = subtotal * tax_rate
    total_bill = subtotal + tax
    
    print(f"Base charge: ${base_charge:.2f}")
    if additional_minutes > 0:
        print(f"Additional minutes charge: ${additional_minutes_cost:.2f}")
    if additional_texts > 0:
        print(f"Additional text messages charge: ${additional_texts_cost:.2f}")
    print(f"911 fee: ${fee_911:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total bill amount: ${total_bill:.2f}")
    
#cell_phone_bill()

