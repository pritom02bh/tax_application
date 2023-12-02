from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database setup
DATABASE = "sqlite_db.db"

def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tax_record (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            amount REAL NOT NULL,
            payment_date DATE NOT NULL,
            status TEXT NOT NULL,
            due_date DATE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Create the table on startup
create_table()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_records')
def get_records():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, company, amount, payment_date, status, due_date FROM tax_record")
    records = cursor.fetchall()
    conn.close()
    return jsonify(records)

@app.route('/search', methods=['POST'])
def search():
    search_id = request.form.get('search_id')
    search_date = request.form.get('search_date')
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    if search_id:
        cursor.execute("SELECT * FROM tax_record WHERE id=?", (search_id,))
    elif search_date:
        cursor.execute("SELECT * FROM tax_record WHERE payment_date=?", (search_date,))
    else:
        return jsonify([])

    records = cursor.fetchall()
    conn.close()
    return jsonify(records)

@app.route('/insert', methods=['POST'])
def insert():
    company = request.form.get('company')
    amount = request.form.get('amount')
    payment_date = request.form.get('payment_date')
    status = request.form.get('status')
    due_date = request.form.get('due_date')

    try:
        # Convert payment_date and due_date to datetime objects
        payment_date = datetime.strptime(payment_date, '%Y-%m-%d').date()
        due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format'})

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tax_record (company, amount, payment_date, status, due_date) VALUES (?, ?, ?, ?, ?)",
                   (company, amount, payment_date, status, due_date))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/delete/<int:record_id>', methods=['DELETE'])
def delete(record_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tax_record WHERE id=?", (record_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})



    # Calculate the total amount for the company
    total_amount = sum(row[2] for row in company_data)

    # Calculate the tax amount
    tax_due = total_amount * tax_rate

    # Prepare the result
    result = {
        'company_data': company_data,
        'total_amount': total_amount,
        'tax_due': tax_due
    }

    conn.close()

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
