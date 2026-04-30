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
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

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
                print(f"Balance: ${data[2]:.2f}")
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

        elif choice == "3":  # Deposit
            user_id = input("Enter ID: ")
            
            # Check if account exists
            cursor.execute("SELECT balance FROM bank_info WHERE id = ?", (user_id,))
            data = cursor.fetchone()
            
            if data:
                amount = float(input("Enter amount to deposit: $"))
                if amount > 0:
                    new_balance = data[0] + amount
                    cursor.execute(
                        "UPDATE bank_info SET balance = ? WHERE id = ?",
                        (new_balance, user_id)
                    )
                    conn.commit()
                    print(f"Deposited ${amount:.2f}. New balance: ${new_balance:.2f}")
                else:
                    print("Amount must be positive.")
            else:
                print("Account not found.")

        elif choice == "4":  # Withdraw
            user_id = input("Enter ID: ")
            
            # Check if account exists
            cursor.execute("SELECT balance FROM bank_info WHERE id = ?", (user_id,))
            data = cursor.fetchone()
            
            if data:
                amount = float(input("Enter amount to withdraw: $"))
                if amount > 0:
                    if amount <= data[0]:
                        new_balance = data[0] - amount
                        cursor.execute(
                            "UPDATE bank_info SET balance = ? WHERE id = ?",
                            (new_balance, user_id)
                        )
                        conn.commit()
                        print(f"Withdrew ${amount:.2f}. New balance: ${new_balance:.2f}")
                    else:
                        print(f"Insufficient funds. Current balance: ${data[0]:.2f}")
                else:
                    print("Amount must be positive.")
            else:
                print("Account not found.")

        elif choice == "5":
            break

    conn.close()


if __name__ == "__main__":
    main()