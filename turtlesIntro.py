#All import statements need to be on top of your program
import turtle

# Create a screen and a turtle object
# creating a variable that will store the screen object
# turtle.Screen you are instantiating a Screen Object

# data types that are objects normally have a behavior attached to it.
# behaviors are functions or methods
screen = turtle.Screen()
screen.title("Turtle Example in Python")

# Create a turtle instance - you are instantiating a Turtle object
my_turtle = turtle.Turtle()

# Draw a square
#  The for loop will loop through the same code 4 times.
# the i represents the loop variable.
for i in range(4):
    #print(i)
    my_turtle.forward(100)  # Move forward by 100 units
    my_turtle.right(90)     # Turn right by 90 degrees

# Keep the window open until clicked
closeWindow = input("Press any key to close window. ")
screen.mainloop()

# Keep the window open until clicked
turtle.done()