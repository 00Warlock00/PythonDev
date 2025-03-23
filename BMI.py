"Create a bmi.py program that calculates your own BMI."

mass = int(input("Enter your mass in kg: "))
height = float(input("Enter your height in m: "))
bmi = mass / height ** 2
print(f"Your BMI is {bmi:.2f}") # 2 decimal places

