import sqlite3

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('sqlite_db.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the 'tax_record' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tax_record (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        company TEXT NOT NULL,
        amount REAL NOT NULL,
        payment_date DATE,
        status TEXT,
        due_date DATE
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
