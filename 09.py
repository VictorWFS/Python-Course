weight = int(input("Weight: "))
unit = input("L for lbs or K for kg: ")

if unit.upper() == 'L':
    converted = weight * 0.45
    print("You are {} kilos" .format(converted))
else:
    converted = weight //0.45
    print("You are {} pounds" .format(converted))

