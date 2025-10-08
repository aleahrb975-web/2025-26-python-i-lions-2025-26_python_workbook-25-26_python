
"""
Exercise 1:  Mailing Address
Create a program that displays your name and complete mailing 
address formatted in the manner that you would usually see it 
on the outside of an envelope.  Your program does not need to 
read any input from the user.  (9 lines)
"""
def address():
    print("Aleah\n8841 Rambling Ridge Dr\nWest Chester, OH, 45069")

address()
"""
Exercise 2:  Hello
Write a program that asks the user to enter his or her name.  
The program should respond with a message that says hello to 
the user, using his or her name.  (9 lines)
"""
def hello(name):
    print("Hello, "+name)
    
hello("Aleah")
"""
Exercise 3:  Area of a Room
Write a program that asks the user to enter the width and 
length or a room.  Once the values have been read, your 
program should compute and display the area of the room.  
The length and the width will be entered as floating point 
numbers.  Include units in your prompt and output message;  
either feet or meters, depending on which unit you are more 
comfortable working with.  (13 lines)
"""
def area(width, length):
    w=float(width)
    l=float(length)
    area=l*w
    print(area)
area(5,6)
"""
Exercise 4:  Area of a Field
Create a program that reads the length and width of a 
farmer’s field from the user in feet.  Display the 
area of the field in acres.  
Hint: There are 43,560 square feet in an acre
"""
def acre(l,w):
    l=float(l)
    w=float(w)
    area=l*w
    acre=area/43560
    print(acre)
    
acre(900,200)
"""
Exercise 5:  Bottle Deposits
In many jurisdictions a small deposit is added to drink 
containers to encourage people to recycle them.  In one 
particular jurisdiction, drink containers holding one liter 
or less have a $0.10 deposit, and drink containers holding 
more than one liter have $0.25 deposit.
Write a program that reads the number of containers of each 
size from the user.  Your program should continue by computing 
and displaying the refund that will be received for returning 
those containers.  Format the output so that it includes a dollar 
sign and always displays exactly two decimal places.  (15 lines)
"""
def bottles():
    small=int(input("How many small bottles?"))
    big=int(input("How mnay big bottles?"))
    money=small*.1
    money=money+big*.25
    print(money)
    
bottles()

def print_hi(name):
    print(f"Hi, {name}")

    """
    if __name__ == "__main__":
    print_hi("Netbeans")
    """

