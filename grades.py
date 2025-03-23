#Create a grades.py program that checks whether a grade is above or below 55.
import random
grade = random.randint(0,100)

if grade > 55:
    print("You passed")

else:
    print("You failed")