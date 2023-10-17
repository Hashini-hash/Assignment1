"""
import random

def roll_dice(num_dice):
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        total += roll
        print(f"Rolled: {roll}")
    return total

def main():
    num_dice = int(input("How many dice to roll? "))
    if num_dice <= 0:
        print("Please enter a positive integer.")
        return

    total = roll_dice(num_dice)
    print(f"Total sum: {total}")

if __name__ == "__main__":
    main()


#quiz 2

def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to quit): ")
        if user_input == "":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return numbers

def main():
    numbers = get_numbers()
    if not numbers:
        print("No numbers were entered.")
        return

    sorted_numbers = sorted(numbers, reverse=True)
    top_five = sorted_numbers[:5]

    print("Top five numbers in descending order:")
    for num in top_five:
        print(num)

if __name__ == "__main__":
    main()

    #quiz 3

def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


def main():
        user_input = input("Enter an integer: ")
        try:
            num = int(user_input)
            if is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
        main()
  """
        #quiz 4
def main():
    cities = []
    for _ in range(5):
        city_name = input("Enter a city name: ")
        cities.append(city_name)


    print("Cities:")
    for city in cities:
        print(city)

if __name__ == "__main__":
        main()





