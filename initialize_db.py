import sqlite3

# Step 1: Connect to a database (this creates it in bank.db file)
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

# Step 2: Create a table called 'bank_info'
cursor.execute('''
    CREATE TABLE bank_info (
        id INTEGER PRIMARY KEY,
        name TEXT;
        account_type TEXT,
        balance INTEGER
    )
''')

# Step 3: Insert 2 bank accounts 
cursor.execute("INSERT INTO bank_info VALUES (1, 'Maria Garcia', 'checking' , 1000)")
cursor.execute("INSERT INTO bank_info VALUES (2, 'James Chen', 'savings' , 2000)")

# IMPORTANT: commit your changes to save them
conn.commit()

# Step 4: Query all bank accounts and print them
cursor.execute("SELECT * FROM bank_info")
rows = cursor.fetchall()

print("All bank accounts:")
for row in rows:
    print(f"  ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

# Clean up
conn.close()