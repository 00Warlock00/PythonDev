# Solution

def weird(num):
    if num % 2 == 1:
        print("Weird")
    elif num % 2 == 0 and 2 <= num <= 5:
        print("Not Weird")
    elif num % 2 == 0 and 6 <= num <= 20:
        print("Weird")
    elif num % 2 == 0 and num > 20:
        print("Not Weird")
    else:
        print("Invalid input")
        return "Invalid input"

weird(3)
weird(24)
weird(20)
weird(4)
weird(5)
weird(2)