import sqlite3

def get_balance_by_id(cursor, user_id):
    cursor.execute('SELECT balance FROM bank_info WHERE id = ?', (user_id,))
    return cursor.fetchone()


def main():
    connection = sqlite3.connect('bank.db')
    cursor = connection.cursor()

    print("=== Bank CLI ===")

    while True:
        user_input = input("\nEnter account ID to view balance (or 'x' to quit): ")

        if user_input.lower() == 'x':
            print("Leaving Marvelous Bank. Thank you for visiting!")
            break

        if not user_input.isdigit():
            print("Invalid input. Please enter a numerical ID.")
            continue

        user_id = int(user_input)
        result = get_balance_by_id(cursor, user_id)

        if result:
            print(f"Balance for account {user_id}: ${result[0]}")
        else:
            print("No account found with that ID.")

    connection.close()


if __name__ == "__main__":
    main()