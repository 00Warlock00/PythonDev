import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    try:
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = calculate_hypotenuse(a, b)
        print(f"The length of the hypotenuse is: {c}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()