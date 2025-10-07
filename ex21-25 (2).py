"""
Exercise 21:  Area of a Triangle
The area of a triangle can be computed using the following formula,
where b is the length of the base of the triangle, and h is its 
height:
        area = (b*h)/2
Write a program that allows the user to enter values for b and h.
The program should then compute and display the area of a triangle
with base length b and height h
"""
def area_of_triangle():
    b = float(input("enter the base of the triangle: "))
    h = float(input("enter the height of the triangle: "))
    area = (b*h)/2
    print("the area of the triangle is: ", area)
    
#area_of_triangle()
"""
Exercise 22: Area of a triangle (Again)
In the previous exercise you created a program that computed the area
of a triangle when the length of its base and its height were known.
It is also possible to compute the area of a triangle when the lengths
of all three sides are known.  Let s1, s2, and s3 be the lengths of the
sides.  Let s = (s1 + s2 + s3)/2.  Then the area of a triangle can be 
calculated using the following formula:

     area = (s * (s - s1) * (s - s2) * (s - s3))**(1/2)

Develop a program that reads the lengths of the sides of a triangle from
the user and display its area.
"""
def area_of_triangle2():
    s1 = float(input("enter the length of side 1: "))
    s2 = float(input("enter the length of side 2: "))
    s3 = float(input("enter the length of side 3: "))
    s = (s1 + s2 + s3)/2
    area = (s * (s - s1) * (s - s2) * (s - s3))**(1/2)
    print("the area of the triangle is: ", area)
    
#area_of_triangle2()

"""
Exercise 23:  Area of a Regular Polygon
A polygon is regular if its sides are all the same length and the angles
between all of the adjacent sides are equal.  The area of a regular polygon
can be computed using the following formula, where s is the length of a side
and n is the number of sides: 
     area = (n * s**(2))/(4 * tan(pi/n))
Write a program that reads s and n from the user and then displays the area
of a regular polygon constructed from these values.
"""
def area_of_polygon():
    from math import tan, pi
    s = float(input("enter the length of a side: "))
    n = int(input("enter the number of sides: "))
    area = (n * s**(2))/(4 * tan(pi/n))
    print("the area of the polygon is: ", area)
#area_of_polygon()
"""
Exercise 24: Units of Time
Create a program that reads a duration from the user as a number of days,
hours, minutes, and seconds.  Compute the total number of seconds represented
by this duration.
"""
def units_of_time():
    days = int(input("enter number of days: "))
    hours = int(input("enter number of hours: "))
    minutes = int(input("enter number of minutes: "))
    seconds = int(input("enter number of seconds: "))
    total_seconds = days*86400 + hours*3600 + minutes*60 + seconds
    print("the total number of seconds is: ", total_seconds)
#units_of_time()

""" 
Exercise 25: Units of Time (again)
In this exercise you will reverse the process described in the previous 
exercise.  Develop a program that begins by reading a number of seconds from 
the user.  Then your program should display the equivalent amount of time 
in the form D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, 
minutes and seconds respectively.  The hours, minutes and seconds should all
be formatted so that they occupy exactly two digits, with a leading 0 displayed
if necessary.
"""
def units_of_time2():
    total_seconds = int(input("enter the total number of seconds: "))
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    print(f"{days}:{hours:02}:{minutes:02}:{seconds:02}")