name = input("Type your name: ")

if (len(name)) < 3:
    print("Name must be at least 3 characters long.")
elif (len(name)) > 50:
    print("Name can be a maximum of 50 characters long")
else:
    print("That's a good name!")