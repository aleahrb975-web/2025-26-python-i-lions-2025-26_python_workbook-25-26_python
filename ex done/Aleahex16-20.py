
"""
Exercise 16:  Area and Volume
Write a program that begins by reading a radius, r, from the user.  The program 
will continue by computing and displaying the area of a circle with radius r 
and the volume of a sphere with radius r.  Use the pi constant in the math 
module in your calculations.

Hint:  The are of  circle is computed using the formula area = pi*r**2.  The 
volume of a sphere is computed using the formula volume = 4/3 * pi * r**3.
"""
import math
def radius():
    r=float(input("What's the radius?"))
    acircle=math.pi*r**2
    asphere=(4/3)*math.pi*r**3
    print("The area of this circle: "+str(acircle))
    print("The area of this sphere: "+str(asphere))
    
#radius()
"""
Exercise 17:  Heat Capacity
The amount of energy required to increase the temperature of one gram of 
material by one degree Celsius is the material’s specific heat capacity, C.  
The total amount of energy required to raise m grams of a material by deltaT 
degrees Celsius can be computed using the formula:  q = mC deltaT.

Write a program that reads the mass of some water and the temperature change 
from the suer.  Your program should display the total amount of energy that 
must be added or removed to achieve the desired temperature change.

Hint:  The specific heat capacity of water is 4.186 J/gC.  Because water has 
a density of 1.0 gram per milliliter, you can use grams and milliliters 
interchangeably in this exercise.

Extend your program so that it also computes the cost of heating the water.  
Electricity is normally billed using units of kilowatt hours rather than Joules.  
In this exercise, you should assume that electricity costs 8.9 cents per 
kilowatt-hour.  Use your program to compute the cost of boiling water for 
a cup of coffee.

Hint:  You will need to look up the factor for converting between Joules 
and kilowatt hours to complete the last part of this exercise.
(25 lines)
"""
def energy():
    mass=float(input("What's the mass of the water?"))
    temperature=float(input("How many degrees C do you want it to change?"))
    q=4.186*mass*temperature
    print(str(q)+" J")

    kilowatthour=float(q)/(3.6e+6)
    cost=kilowatthour*8.9
    money=round((cost/100), 3)
    print("The cost of boiling this water is: $"+str(money))

#energy()
"""
Exercise 18:  Volume of a Cylinder
The volume of a cylinder can be computed by multiplying the area of its 
circular base by its height.  Write a program that reads the radius of the 
cylinder, along with its height, from the user and computes its volume.  
Display the result rounded to one decimal place.
(15 lines)
"""
def volume():
    r=float(input("What's the radius?"))
    h=float(input("What's the height"))
    base=math.pi*r**2
    volume=base*h
    print("the volume is: "+str(volume))
    
#volume()
"""
Exercise 19:  Free Fall
Create a program that determines how quickly an object is traveling when it 
hits the ground.  The user will enter the height from which the object is 
dropped in meters (m).  Because the object is dropped its initial speed is 
0 m/s.  Assume that the acceleration due to gravity is 9.8 m/s**2.  You can 
use the formula vf = (vi**2 + 2ad)**(1/2) to compute the final speed vf, 
when the initial speed, vi, acceleration, a, and distance, d, are known.
(16 lines)
"""
def speed():
    h=float(input("How high is it in meters?"))
    final=(0**2+2*9.8*h)**(1/2)
    print(str(final)+ " m/s")
    
#speed()
"""
Exercise 20: Ideal Gas Law
The ideal gas law is a mathematical approximation of the behavior of gasses as 
pressure, volume and temperature change.  It is usually stated as:

PV = nRT
pressure*volume=moles*8.314*temp
Where P is the pressure in Pascals, V is the volume in liters, n in the amount 
of substance in moles, R is the ideal gas constant, equal to 8.314 J/molK, and 
T is the temperature is Kelvin.

Write a program that computes the amount of gas in moles when the user supplies 
the pressure, volume and temperature.  Test your program by determining the 
number of moles of gas in a SCUBA tank.  A typical SCUBA tank holds 12 liters 
of gas at a pressure of 20,000,000 Pascals (approximately 3,000 PSI).  
Room temperature is approximately 20 degrees Celsius or 68 degrees Fahrenheit.

Hint:  A temperature is converted from Celsius to Kelvin by adding 273.15 to it.  
To convert a temperature from Fahrenheit to Kelvin, deduct 32 from it, multiply 
by 5/9 and then add 273.15 to it.

(19 lines)
"""
def gas():
    p=float(input("Pressure:"))
    v=float(input("Volume:"))
    t=float(input("Temperature:"))
    moles=(p*v)/(8.314*t)
    print(str(moles)+" moles")

def kelvin():
    c=float(input("temp"))
    kelvin=c+273.15
    print(kelvin)
kelvin()
gas()
    
if __name__ == "__main__":
    print("Hi there!")