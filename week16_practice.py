import sqlite3

def initialize_database():
    conn = sqlite3.connect("store_management.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            product_name TEXT NOT NULL,
            amount REAL NOT NULL,
            status TEXT DEFAULT 'Pending',
            FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
        )
    """)

    conn.commit()
    conn.close()
    print("Database and tables initialized successfully!")

def insert_sample_data():
    conn = sqlite3.connect("store_management.db")
    cursor = conn.cursor()

    customers = [
        ("Alice Smith", "alice@example.com", "555-0101"),
        ("Bob Jones", "bob@example.com", "555-0202")
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO customers (name, email, phone)
        VALUES (?, ?, ?)
    """, customers)

    orders = [
        (1, "Laptop", 1200.50, "Completed"),
        (1, "Wireless Mouse", 25.99, "Pending"),
        (2, "Standing Desk", 350.00, "Processing")
    ]
    cursor.executemany("""
        INSERT INTO orders (customer_id, product_name, amount, status)
        VALUES (?, ?, ?, ?)
    """, orders)

    conn.commit()
    conn.close()
    print("Sample data inserted successfully!")

def view_customer_orders():
    conn = sqlite3.connect("store_management.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT customers.name, orders.product_name, orders.amount, orders.status
        FROM customers
        JOIN orders ON customers.customer_id = orders.customer_id
    """)
    
    results = cursor.fetchall()
    print("\n--- Customer Orders Report ---")
    for row in results:
        print(f"Customer: {row[0]} | Product: {row[1]} | Amount: ${row[2]} | Status: {row[3]}")

    conn.close()

if __name__ == "__main__":
    initialize_database()
    insert_sample_data()
    view_customer_orders()