# WEEK 16: Capstone Project - Store Management System with Streamlit & SQLite

import sqlite3
import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Store Management Dashboard", layout="wide")

# --- DATABASE SETUP ---
def get_connection():
    return sqlite3.connect("store_management.db")

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Customers Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT
        )
    """)
    
    # Orders Table
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

# Initialize tables on load
initialize_database()

# --- STREAMLIT USER INTERFACE ---
st.title("🛒 Store Manager Dashboard (Capstone Project)")
st.write("Welcome to your Week 16 Capstone! Manage customers and track orders live using SQLite and Streamlit.")

# Sidebar Controls for Adding Data
st.sidebar.header("➕ Add New Customer / Order")

with st.sidebar.form("store_form"):
    cust_name = st.text_input("Customer Name", "Alice Smith")
    cust_email = st.text_input("Customer Email", "alice@example.com")
    cust_phone = st.text_input("Phone Number", "555-0199")
    
    product = st.text_input("Product Name", "Laptop")
    amount = st.number_input("Order Amount ($)", min_value=1.0, value=999.99)
    
    submit_button = st.form_submit_button("Save to Database")
    
    if submit_button:
        conn = get_connection()
        cursor = conn.cursor()
        try:
            # 1. Insert or ignore customer
            cursor.execute("""
                INSERT OR IGNORE INTO customers (name, email, phone) 
                VALUES (?, ?, ?)
            """, (cust_name, cust_email, cust_phone))
            
            # 2. Get the customer_id
            cursor.execute("SELECT customer_id FROM customers WHERE email = ?", (cust_email,))
            cust_id = cursor.fetchone()[0]
            
            # 3. Insert the order linked to this customer
            cursor.execute("""
                INSERT INTO orders (customer_id, product_name, amount, status) 
                VALUES (?, ?, ?, 'Completed')
            """, (cust_id, product, amount))
            
            conn.commit()
            st.sidebar.success(f"Successfully added order for {cust_name}!")
        except Exception as e:
            st.sidebar.error(f"Error: {e}")
        finally:
            conn.close()

# --- MAIN DASHBOARD LAYOUT ---
col1, col2 = st.columns(2)

conn = get_connection()

with col1:
    st.subheader("👥 Customer Directory")
    customers_df = pd.read_sql("SELECT * FROM customers", conn)
    st.dataframe(customers_df, use_container_width=True)

with col2:
    st.subheader("📦 Orders Report")
    orders_query = """
        SELECT o.order_id, c.name AS customer_name, o.product_name, o.amount, o.status
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
    """
    orders_df = pd.read_sql(orders_query, conn)
    st.dataframe(orders_df, use_container_width=True)

conn.close()