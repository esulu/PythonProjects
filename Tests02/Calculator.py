# Python Calculator
# Made by Eren Sulutas 6/28/2018

print("Welcome to Eren's Calculator Program\n")

while True:
    print("\nOptions: \nType \"add\" to add two numbers \nType \"subtract\" to subtract two numbers \nType \"multiply\" to "
          "multiply two numbers \nType \"divide\" to divide two numbers \nType \"quit\" to exit the program")
    entry = input("Entry: ")
    result = 0

    if entry == "add":
        # Addition calculation
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        result = num1 + num2
    elif entry == "subtract":
        # Subtraction calculation
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        result = num1 - num2
    elif entry == "multiply":
        # Multiplication calculation
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        result = num1 * num2
    elif entry == "divide":
        # Division calculation
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        result = num1 / num2
    elif entry == "quit":
        # Exits the program
        break
    else:
        print("Error: Invalid entry.")

    print("Result: " + str(result))

print("\nEnd of program")