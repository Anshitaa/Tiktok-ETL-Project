import psycopg2
import json
from datetime import datetime

# Load orders from JSON
with open("data/tiktok_orders.json") as f:
    orders = json.load(f)

print(f"📦 Loaded {len(orders)} orders from JSON.")

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1110",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    print("🟢 Connected to PostgreSQL.")
except Exception as e:
    print("❌ Failed to connect to database:", e)
    exit()

# Helper: Get or insert customer
def get_or_create_customer(name):
    cur.execute("SELECT customer_id FROM customers WHERE name=%s", (name,))
    result = cur.fetchone()
    if result:
        return result[0]
    cur.execute("INSERT INTO customers (name) VALUES (%s) RETURNING customer_id", (name,))
    return cur.fetchone()[0]

# Helper: Get or insert product
def get_or_create_product(name, price):
    cur.execute("SELECT product_id FROM products WHERE name=%s", (name,))
    result = cur.fetchone()
    if result:
        return result[0]
    cur.execute("INSERT INTO products (name, price) VALUES (%s, %s) RETURNING product_id", (name, price))
    return cur.fetchone()[0]

print("🚀 Inserting records into PostgreSQL...")

# Insert each order
for order in orders:
    cust_id = get_or_create_customer(order['customer'])
    prod_id = get_or_create_product(order['product'], order['price'])

    cur.execute("""
        INSERT INTO orders (order_id, customer_id, product_id, quantity, order_time)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING
    """, (
        order['order_id'], cust_id, prod_id, order['quantity'],
        datetime.fromisoformat(order['timestamp'])
    ))

conn.commit()
cur.close()
conn.close()

print("✅ Orders loaded into PostgreSQL.")

