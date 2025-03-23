Gryffindor =0
Ravenclaw = 0
Hufflepuff =0
Slytherin = 0




while True:
  try:
    print("Welcome to the Hogwarts House Election!")
    print(f" 1) Gryffindor")
    print(f" 2) Ravenclaw ")
    print(f" 3) Hufflepuff")
    print(f" 4) Slytherin")
    house = int(input("Which animal do you prefer? "))

    while True:
     if house < 1 or house > 5:
        print("Invalid house")
        break
     if house == 1:
            Gryffindor += 1
            break
     if house == 2:
            Ravenclaw += 1
            break
     if house == 3:
            Hufflepuff += 1
            break
     if house == 4:
            Slytherin += 1
     elif house == 4:
            Slytherin += 1
            break
     elif house == 5:
            print("bay")
            break
     else:
            print("Invalid house")
            break
  except ValueError:
    print("Invalid input")

#Score


score = Score()
print(f"Your score is: {score.score}")
print(f"Gryffindor: {Gryffindor}")
print(f"Ravenclaw: {Ravenclaw}")
print(f"Hufflepuff: {Hufflepuff}")
print(f"Slytherin: {Slytherin}")

