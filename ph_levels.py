#Create a ph_levels.py program that checks whether a pH level is basic, acidic, or neutral.

try:
 ph = int(input("Enter the pH level between 1 to 14: "))

 while ph > 0 and ph < 14:
  if ph < 7:
    print("Basic")
    break
  elif ph < 7:
    print("Acidid")
    break
  else:
      print("Neutral")
      break
except:
    print("Invalid input. Please enter a number between 1 and 14.")