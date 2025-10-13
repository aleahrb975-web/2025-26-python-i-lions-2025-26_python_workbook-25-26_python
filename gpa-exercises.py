"""
Exercise 51:  Letter Grade to Grade Points

At a particular university, letter grades are mapped to grade
points in the following manner:

Letter                  Grade points
A+                      4.0
A                       4.0
A-                      3.7
B+                      3.3
B                       3.0
B-                      2.7
C+                      2.3
C                       2.0
C-                      1.7
D+                      1.3
D                       1.0
F                       0


Write a program that begins by reading a letter grade from the 
user.  Then your program should compute and display the equivalent
number of grade points.  Ensure that your program generates an 
appropriate error message if the user enters an invalid letter
grade.
"""
def letter_to_grade_points():
    grade_mapping = {
        "A+": 4.0,
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "C-": 1.7,
        "D+": 1.3,
        "D": 1.0,
        "F": 0.0
    }
    
    letter_grade = input("Enter a letter grade (e.g., A, B+, C-): ").strip()
    
    if letter_grade in grade_mapping:
        print(f"The equivalent number of grade points for {letter_grade} is {grade_mapping[letter_grade]}.")
    else:
        print("Error: Invalid letter grade entered.")

"""
Exercise 52:  In the previous exercises you created a program that
converts a letter grade into the equivalent number of grade points.
In this exercise you will create a program that reverses the process
and converts from a grade point value entered by the user to a letter
grade.  Ensure that your program handles grade point values that fall
between letter grades.  These should be rounded to the closes letter
grade.  Your program should report A+ for a 4.0 (or greater) grade
point average.
"""
def percentage_to_letter():
    grade_mapping = [
        (4.0, "A+"),
        (3.85, "A"),
        (3.5, "A-"),
        (3.15, "B+"),
        (2.85, "B"),
        (2.5, "B-"),
        (2.15, "C+"),
        (1.85, "C"),
        (1.5, "C-"),
        (1.15, "D+"),
        (0.85, "D"),
        (0.0, "F")
    ]
    
    try:
        grade_point = float(input("Enter a grade point value (e.g., 3.7): ").strip())
        
        if grade_point >= 4.0:
            print("The equivalent letter grade is A+.")
            return
        
        for point, letter in grade_mapping:
            if grade_point >= point:
                print(f"The equivalent letter grade is {letter}.")
                return
        
        print("The equivalent letter grade is F.")
        
    except ValueError:
        print("Error: Invalid input. Please enter a numeric grade point value.")
        
        
"""
Exercise 66:  Compute a Grade Point Average
Exercise 51 includes a table that shows the conversion from letter
grades to grade points at a particular academic institution.  In this
exercise you will compute the grade point average of an arbitrary number
of letter grades entered by teh user.  The user will enter a blank
line to indicate that all of the grades have been provided.  For example,
if the user enters A, followed by C+, followed by B, followed by a blank
line then your program should report a grade point average of 3.1.
You may find your solutions to Exercise 51 helpful when completing this 
exercise.  Your program does not need to do any error checking.  It can
assume that each value entered by the user will be a valid letter grade
or a blank line.
"""

def compute_gpa():
    grade_mapping = {
        "A+": 4.0,
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "C-": 1.7,
        "D+": 1.3,
        "D": 1.0,
        "F": 0.0
    }
    
    total_points = 0.0
    count = 0
    
    while True:
        letter_grade = input("Enter a letter grade (or press Enter to finish): ").strip()
        
        if letter_grade == "":
            break
        
        if letter_grade in grade_mapping:
            total_points += grade_mapping[letter_grade]
            count += 1
        else:
            print("Invalid letter grade entered. Please try again.")
    
    if count > 0:
        gpa = total_points / count
        print(f"The grade point average is {gpa:.2f}.")
    else:
        print("No grades were entered.")
        
        
compute_gpa()
