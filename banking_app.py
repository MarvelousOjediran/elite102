import sqlite3

# Connect to your database file (creates bank_info.db if it doesn't exist)
conn = sqlite3.connect('bank_info.db')
cursor = conn.cursor()

# Create your bank_info table (matching your existing table)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bank_info (
        id INTEGER PRIMARY KEY,
        customer_name TEXT,
        balance REAL
    )
''')

# Insert some sample data
cursor.execute("INSERT OR REPLACE INTO bank_info VALUES (1, 'Alice Johnson', 1500.75)")
cursor.execute("INSERT OR REPLACE INTO bank_info VALUES (2, 'Bob Smith', 3200.50)")
conn.commit()



# You can also query everything
cursor.execute("SELECT * FROM bank_info")
all_rows = cursor.fetchall()

print("\nComplete bank records:")
for row in all_rows:
    print(f"  ID: {row[0]}, Name: {row[1]}, Balance: ${row[2]}")


# Query only the balance column (what you asked about earlier)
cursor.execute("SELECT balance FROM bank_info")
balances = cursor.fetchall()

print("All bank balances:")
for balance in balances:
    print(f"  ${balance[0]}")    

# Always close the connection
conn.close() 

