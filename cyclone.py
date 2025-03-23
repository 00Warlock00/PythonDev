#Ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variable.

height = int(input("What is your height in cm? "))
credits = int(input("How many credits do you have? "))

#If the user is at least 137 cm tall and has at least 10 credits, print "Enjoy the ride!"

if height >= 137 and credits >= 10:
    print("Enjoy the ride!")

elif height < 137 and credits >= 10:
    print("You are not tall enough to ride.")

elif height >= 137 and credits < 10:
 print("You do not have enough credits.")

else:
    print("You are not tall enough to ride and you do not have enough credits.")
