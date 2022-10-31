import random

print("*********************************")
print("Welcome to the guessing game!")
print("*********************************")

secret_number = random.randrange(1,101)
total_attempts = 0
spots = 1000

print("What level of difficulty?")
print("(1) Easy (2) Medium (3) Difficult")

level = int(input("Set the level: "))

if(level == 1):
    total_attempts = 20
elif(level == 2):
    total_attempts = 10
else:
    total_attempts = 5

for game in range(1, total_attempts + 1):
    print("Try", game, " of ", total_attempts)
    
    kick_str = input("Enter your number: ")
    print("You typed " , kick_str)
    kick = int(kick_str)

    if(kick < 1 or kick > 100):
        print("You must enter a number between 1 and 100!")
        continue

    hit = kick == secret_number
    larger = kick > secret_number
    minor = kick < secret_number
    print(secret_number)
    print(larger, minor)
    if(hit):
        print("You got it right and got {} points!".format(spots))
        break
    else:
        if(larger):
            print("Your guess was bigger than the secret number!")
        elif(minor):
            print("Your guess was less than the secret number!")
        lost_points = abs(secret_number - kick) #40-20 = 20 / number absolut: 40-60 = -20, romove the netagtive with abs()
        spots = spots - lost_points

print("End of the game")