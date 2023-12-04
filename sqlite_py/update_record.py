import sqlite3
from datetime import date

# Connect to SQLite database
conn = sqlite3.connect('sqlite_db.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Update due_date for a specific row where id is 1
row_id_to_update = 44
new_due_date = date(2024, 6, 15)

# Execute the update query
cursor.execute('''
    UPDATE tax_record
    SET due_date = ?
    WHERE id = ?
''', (new_due_date, row_id_to_update))

# Commit the changes and close the connection
conn.commit()
conn.close()
