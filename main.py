import sqlite3


def main():
    connection = sqlite3.connect('bank.db')
    cursor = connection.cursor()

    # Get all rows from the students table
    print("Fetching all rows from the bank database...")
    results = cursor.execute('''
        SELECT * FROM bank_info
    ''')

    print("Results:")
    for row in results:
        print(row)

    # Get all students with a GPA greater than 3.5
    print("Fetching total bank account balances")
    results = cursor.execute('''
        SELECT balance FROM bank_info;
    ''')
    print("Results:")
    for row in results:
        print(row)

    connection.close()


if __name__ == "__main__":
    main()
