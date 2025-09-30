import turtle

#screen is an object of the Screen class
screen = turtle.Screen()
screen.title("Clock Turtle")
screen.bgcolor("lightgreen")

#poly is an object of the Turtle class
poly = turtle.Turtle()
poly.shape("turtle")
poly.color("blue")

def draw_clock():
    for i in range(12):
        poly.stamp()
        poly.penup()
        poly.forward(150)
        poly.pendown()
        poly.stamp()
        poly.backward(150)
        poly.right(30)

draw_clock()

screen.listen()
screen.mainloop()

