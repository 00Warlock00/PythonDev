import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_square_area(side):
    return side ** 2

def calculate_triangle_area(base, height):
    return 0.5 * base * height
def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

while True:

 print("-----------------------------------")
 print("-----------------------------------")
 print("Area Calculator")
 print("-----------------------------------")
 print("-----------------------------------")

 print("Triangle (t)")
 print("Retangle (r)")
 print("Square   (s)")
 print("Circles  (c)")
 print("Exit     (e)")

 # Ask the user for the shape
 shape = input("Enter the shape: ")

 if shape == "e":
    print("exiting the calculator. Good Bay!")
    break
 elif shape == "t":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    print(f"The area of the triangle is: {calculate_triangle_area(base, height)}")
 elif shape == "r":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    print(f"The area of the rectangle is: {calculate_rectangle_area(length, width)}")
 elif shape == "s":
    side = float(input("Enter the side: "))
    print(f"The area of the square is: {calculate_square_area(side)}")
 elif shape == "c":
    radius = float(input("Enter the radius: "))
    print(f"The area of the circle is: {calculate_circle_area(radius)}")
    print(f"The perimeter of the circle is: {calculate_circle_perimeter(radius)}")
else:
    print("Invalid shape. Please try again.")
