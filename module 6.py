#quiz 1
"""
import random

def roll_dice():
    return random.randint(1, 6)

def main():
    rolls = 0
    while True:
        result = roll_dice()
        rolls += 1
        print(f"Roll {rolls}: {result}")
        if result == 6:
            break

if __name__ == "__main__":
    main()

    #quiz 3
def gallons_to_liters(gallons):
        liters = gallons * 3.78541  # Conversion factor from gallons to liters
        return liters


def main():
        while True:
            try:
                gallons = float(input("Enter a quantity in gallons (negative value to quit): "))
                if gallons < 0:
                    break
                liters = gallons_to_liters(gallons)
                print(f"{gallons} gallons is approximately {liters:.2f} liters.")
            except ValueError:
                print("Invalid input. Please enter a number.")


if __name__ == "__main__":
        main()

#quiz4

def sum_of_list(numbers):
    total = sum(numbers)
    return total

def main():

    numbers = [1, 2, 3, 4, 5]


    total_sum = sum_of_list(numbers)


    print(f"The sum of the numbers is: {total_sum}")

if __name__ == "__main__":
    main()



#quiz 5

def remove_odd_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

def main():

    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    even_numbers_list = remove_odd_numbers(original_list)


    print(f"Original List: {original_list}")
    print(f"List with Odd Numbers Removed: {even_numbers_list}")

if __name__ == "__main__":
    main()
"""
#quiz 6

import math

def unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    unit_price = price / area * 10000
    return unit_price

def main():

    diameter1 = float(input("Enter the diameter of pizza 1 (in centimeters): "))
    price1 = float(input("Enter the price of pizza 1 (in euros): "))


    diameter2 = float(input("Enter the diameter of pizza 2 (in centimeters): "))
    price2 = float(input("Enter the price of pizza 2 (in euros): "))


    unit_price1 = unit_price(diameter1, price1)
    unit_price2 = unit_price(diameter2, price2)


    if unit_price1 < unit_price2:
        print("Pizza 1 provides better value for money.")
    elif unit_price1 > unit_price2:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas have the same unit price.")

if __name__ == "__main__":
    main()











