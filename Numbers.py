# a program that checks whether a number is zero, positive or negative
try:
    number = float(input('Enter a number: '))

    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

except ValueError:
    print("Invalid input. Please enter a valid number.")
