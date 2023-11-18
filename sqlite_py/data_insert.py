import sqlite3
from datetime import date

# Connect to SQLite database
conn = sqlite3.connect('sqlite_db.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Sample data to insert
data_to_insert = [
    ('derm', 4100, date(2023, 9, 26), 'paid', None),
    ('derm', 4100, date(2023, 10, 12), 'paid', None),
    ('tek', 15200, date(2023, 6, 9), 'Paid', None),
    ('tek', 15200, date(2023, 7, 12), 'Paid', None),
    ('tek', 11400, date(2023, 8, 11), 'Paid', None),
    ('tek', 14440, date(2023, 9, 21), 'Paid', None),
    ('tek', 15200, date(2023, 10, 18), 'Paid', None),
    ('tek', 23520, None, 'Paid', None),
    ('tek', 16800, None,'Paid', None),
    ('tek', 16800, None, 'Paid', None),
    ('tek', 16800, None, 'Paid', None)
]

# Insert data into the 'tax_record' table
cursor.executemany('''
    INSERT INTO tax_record (company, amount, payment_date, status, due_date)
    VALUES (?, ?, ?, ?, ?)
''', data_to_insert)

# Commit the changes and close the connection
conn.commit()
conn.close()
