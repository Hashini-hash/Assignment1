# quiz1
number = 1

while number <= 1000:

    if number % 3 == 0:

        print(number)

    number += 1

#quiz2
inch = 2.54

while True:

    inches = float(input("Enter a length in inches: "))


    if inches < 0:
        print("Program has ended.")
        break

    centimeters = inches * inch
    print(f"{inches} inches is equal to {centimeters} centimeters")

#quiz4
import random

num = random.randint(1,10)
guess = 0

while guess != num:
    guess = int(input("Enter any number:"))

    if guess < num:
        print("too low")


    elif guess > num:
        print("too high")


    else:
        print("Correct")

#quiz3

def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return numbers

def find_smallest_and_largest(numbers):
    if not numbers:
        return None, None
    smallest = largest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
    return smallest, largest

if __name__ == "__main__":
    numbers = get_numbers()
    smallest, largest = find_smallest_and_largest(numbers)

    if smallest is not None and largest is not None:
        print(f"The smallest number is: {smallest}")
        print(f"The largest number is: {largest}")
    else:
        print("No valid numbers were entered.")




#quiz5

def login():
    username = "python"
    password = "rulesinpython"
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        entered_username = input("Enter username: ")
        entered_password = input("Enter password: ")

        if entered_username == username and entered_password == password:
            print("Welcome")
            return

        print("Incorrect username or password. Please try again.")
        attempts += 1

    print("Access denied")

if __name__ == "__main__":
    login()





