#quiz 1
"""
def get_season(month):
    seasons = ('Winter', 'Spring', 'Summer', 'Autumn')
    month_to_season = {
        1: 'Winter', 2: 'Winter', 3: 'Spring',
        4: 'Spring', 5: 'Spring', 6: 'Summer',
        7: 'Summer', 8: 'Summer', 9: 'Autumn',
        10: 'Autumn', 11: 'Autumn', 12: 'Winter'
    }
    return month_to_season.get(month, 'Invalid month')

def main():
    month = int(input("Enter a number of a month (1-12): "))
    if 1 <= month <= 12:
        season = get_season(month)
        print(f"The season corresponding to month {month} is {season}.")
    else:
        print("Invalid month. Please enter a number between 1 and 12.")

if __name__ == "__main__":
    main()
"""
#quiz 2
def main():
    names_set = set()
    while True:
        user_input = input("Enter a name (or press Enter to quit): ")
        if user_input == "":
            break

        if user_input in names_set:
            print(f"Existing name: {user_input}")
        else:
            print(f"New name: {user_input}")
            names_set.add(user_input)

    print("\nInput Names:")
    for name in names_set:
        print(name)

if __name__ == "__main__":
    main()









