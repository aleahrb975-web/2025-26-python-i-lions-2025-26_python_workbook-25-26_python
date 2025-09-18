import turtle

#Screen is a complex data type - 
# meaning that it has attributes and behaviors
screen = turtle.Screen() #this is the instantiation call for the object screen
screen.title("Turtle Example in Python")

# Create a turtle object
#Turtle is a complex data type 
poly = turtle.Turtle() #This is the instantiation of an object
poly.color("red")
poly.shape("turtle")

# Move the turtle forward by 100 units
# --forward100 is a non-fruitful function because it does
#   not return a value, it simply performs an action,
#   which is to move the turtle forward 100
def forward100():
    poly.forward(100)

# Turn the turtle to the right by 90 degrees
# --right90 is a non-fruitful function because it does
#   not return a value, it simply performs an action,
#   which is to turn the turtle 90 degrees to the right
def right90():
    poly.right(90)

def make_circle():
    poly.circle(50)

#screen is a Screen object and it has behaviors
# like onkey, onkeypress
screen.onkey(forward100, "Up")
screen.onkey(right90, "Right")
screen.onkeypress(make_circle, "Space")

screen.listen()
screen.mainloop()

# Keep the window open until clicked
turtle.done()