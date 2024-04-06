# create_database.py
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('suppliers.db')
cursor = conn.cursor()

# Create the suppliers table
cursor.execute("""
    CREATE TABLE suppliers (
        supplier TEXT PRIMARY KEY,
        key TEXT NOT NULL
    )
""")

# Insert a list of suppliers and their keys
suppliers = [
    ('Supplier1', 'key1'),
    ('Supplier2', 'key2'),
    # Add more suppliers as needed
]

cursor.executemany("""
    INSERT INTO suppliers (supplier, key) VALUES (?, ?)
""", suppliers)

# Commit the changes and close the connection
conn.commit()
conn.close()