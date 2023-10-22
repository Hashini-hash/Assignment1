#quiz1


import mysql.connector

def fetch_airport_details(icao_code):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port='3306',
        user='root',
        password='Hashini',
        database='flight_game'
    )

    cursor = connection.cursor()


    cursor.execute('SELECT name, municipality FROM airport WHERE ident=%s', (icao_code,))
    result = cursor.fetchone()

    connection.close()

    return result

def main():
    icao_code = input("Enter the ICAO code of the airport: ")
    airport_details = fetch_airport_details(icao_code)

    if airport_details:
        name, location = airport_details
        print(f"Airport Name: {name}")
        print(f"Location (Town): {location}")
    else:
        print(f"No airport found with ICAO code: {icao_code}")

if __name__ == "__main__":
    main()

#quiz2

import mysql.connector
def fetch_airports_by_country_and_type(country_code):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port='3306',
        user='root',
        password='Hashini',
        database='flight_game'
    )

    cursor = connection.cursor()
    cursor.execute('''
            SELECT airport_type, COUNT(*) as count 
            FROM airports 
            WHERE country_code = %s 
            GROUP BY airport_type 
            ORDER BY airport_type
        ''', (country_code,))

    result = cursor.fetchall()

    connection.close()

    return result


def main():
    country_code = input("Enter the country code (): ")
    airports_by_type = fetch_airports_by_country_and_type(country_code)

    if airports_by_type:
        print(f"Aiports in {country_code}:")
        for airport_type, count in airports_by_type:
            print(f"{count} {airport_type} airports")
    else:
        print(f"No airports found for country code: {country_code}")


if __name__ == "__main__":
    main()










