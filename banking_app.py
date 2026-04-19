import sqlite3

def connect():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bank_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            account_type TEXT,
            balance REAL
        )
    ''')

    conn.commit()
    return conn, cursor


def main():
    conn, cursor = connect()

    while True:
        print("\n1. View account")
        print("2. Add account")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            user_id = input("Enter ID: ")

            cursor.execute(
                "SELECT customer_name, account_type, balance FROM bank_info WHERE id = ?",
                (user_id,)
            )

            data = cursor.fetchone()

            if data:
                print(f"\nName: {data[0]}")
                print(f"Type: {data[1]}")
                print(f"Balance: ${data[2]}")
            else:
                print("Account not found.")

        elif choice == "2":
            name = input("Name: ")
            acc_type = input("Account type: ")
            balance = float(input("Balance: "))

            cursor.execute(
                "INSERT INTO bank_info (customer_name, account_type, balance) VALUES (?, ?, ?)",
                (name, acc_type, balance)
            )

            conn.commit()
            print("Account added!")

        elif choice == "3":
            break

    conn.close()


if __name__ == "__main__":
    main()