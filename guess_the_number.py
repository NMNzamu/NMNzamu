import random
number = random.randint(1,10)
print("Guess a random number from 1 to 10")
guess = None
while guess!=number:
        guess = int(input())
        if int(guess)<number:
            print("Too low, try again")
            break
        elif int(guess)>number:
            print ("Too high, try again")
            break
        else:
            print("correct")
            print(f"My random number is {number}")
            print("Good Guess!")
        continue
