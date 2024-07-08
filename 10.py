right_guess = 9
i = 1
while i <= 3:
    guess = int(input("Guess: "))
    if guess == right_guess:
        print("Congratulations! Right guess!!")
        break
    else:
        print("WRONG")
    i = i + 1

