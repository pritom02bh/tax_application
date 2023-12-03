import sqlite3
from datetime import date

# Connect to SQLite database
conn = sqlite3.connect('sqlite_db.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Update records where due_date is NULL
due_date = date(2023, 12, 31)  # Specify the desired date

cursor.execute('''
    UPDATE tax_record
    SET due_date = ?
    WHERE due_date IS NULL
''', (due_date,))

# Commit the changes and close the connection
conn.commit()
conn.close()
