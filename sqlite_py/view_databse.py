import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('sqlite_db.db')
cursor = conn.cursor()

# Select all records from the 'tax_record' table
cursor.execute('SELECT * FROM tax_record')

# Fetch all records
records = cursor.fetchall()

# Print the records
for record in records:
    print(record)

# Close the connection
conn.close()
