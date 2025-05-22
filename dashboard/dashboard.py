import streamlit as st
import psycopg2
import pandas as pd

# --- PostgreSQL Connection ---
def get_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1110",  
        host="localhost",
        port="5432"
    )

# --- Load Data into DataFrames ---
@st.cache_data
def load_data():
    conn = get_connection()
    
    revenue_by_product = pd.read_sql("""
        SELECT p.name AS product, SUM(p.price * o.quantity) AS revenue
        FROM orders o
        JOIN products p ON o.product_id = p.product_id
        GROUP BY p.name
        ORDER BY revenue DESC;
    """, conn)

    daily_revenue = pd.read_sql("""
        SELECT DATE(order_time) AS day, SUM(p.price * o.quantity) AS revenue
        FROM orders o
        JOIN products p ON o.product_id = p.product_id
        GROUP BY day
        ORDER BY day;
    """, conn)

    top_customers = pd.read_sql("""
        SELECT c.name AS customer, SUM(p.price * o.quantity) AS total_spent
        FROM orders o
        JOIN products p ON o.product_id = p.product_id
        JOIN customers c ON o.customer_id = c.customer_id
        GROUP BY c.name
        ORDER BY total_spent DESC
        LIMIT 10;
    """, conn)

    conn.close()
    return revenue_by_product, daily_revenue, top_customers

# --- Streamlit UI ---
st.title("📊 TikTok Shop Order Analytics")

revenue_by_product, daily_revenue, top_customers = load_data()

# Revenue by Product
st.subheader("💄 Revenue by Product")
st.bar_chart(revenue_by_product.set_index("product"))

# Daily Revenue Trend
st.subheader("📅 Daily Revenue")
st.line_chart(daily_revenue.set_index("day"))

# Top Customers
st.subheader("👑 Top Customers")
st.dataframe(top_customers)

st.caption("Built by Anshita Bhardwaj — inspired by Sugar AI’s backend challenges.")

