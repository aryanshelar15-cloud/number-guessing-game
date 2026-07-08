import random

number = random.randint(1, 100)

for i in range(5):
    guess = int(input("Enter your number: "))

    if number == guess:
        print("You win!")
        break

    elif guess < number:
        if number - guess <= 10:
            print("Your guess is low.")
        else:
            print("Your guess is too low.")

    else:
        if guess - number <= 10:
            print("Your guess is high.")
        else:
            print("Your guess is too high.")

print("The correct number is:", number)
