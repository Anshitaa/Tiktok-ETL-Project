
# 🛍️ TikTok Shop ETL & Analytics Project

This project simulates a real-world ETL pipeline and dashboard for TikTok Shop-style eCommerce data. It showcases data generation, PostgreSQL integration, and an interactive Streamlit dashboard for analytics.

---

## 🔧 What It Does

- Generates fake TikTok Shop orders using Python & Faker
- Loads data into a PostgreSQL database using an ETL script
- Runs analytics queries to summarize trends
- Visualizes metrics like top customers, product sales, and revenue over time using Streamlit

---



##  Project Structure

```
tiktok-shop-etl-project/
├── data/                  # Fake order data generator
│   ├── generate_data.py
│   └── tiktok_orders.json
├── etl/                   # ETL pipeline to PostgreSQL
│   └── load_data.py
├── sql/                   # SQL schema + analytics queries
│   ├── schema.sql
│   └── queries.sql
├── dashboard/             # Streamlit analytics dashboard
│   └── dashboard.py
├── requirements.txt       # Python dependencies
└── README.md              # You're reading it!
```




##  Key Features

✅ **Faker-based synthetic TikTok Shop orders**  
✅ **ETL pipeline in Python with psycopg2**  
✅ **PostgreSQL database schema for `orders`, `customers`, and `products`**  
✅ **Streamlit dashboard with analytics**  
✅ Clean modular code and clear directory structure

---

##  Getting Started

### 1️⃣ Clone the repo

```bash
git clone https://github.com/Anshitaa/Tiktok-ETL-Project.git
cd Tiktok-ETL-Project
```
2️⃣ Set up your environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3️⃣ Generate fake TikTok Shop orders
```bash
Copy
python data/generate_data.py
```
4️⃣ Create PostgreSQL tables
```
psql -U postgres -d postgres -f sql/schema.sql
```
5️⃣ Load data into the database
```
python etl/load_data.py
```
6️⃣ Launch the dashboard
```
streamlit run dashboard/dashboard.py
```
📊 Dashboard Preview
The dashboard displays:

🛒 Revenue by product

📅 Daily revenue trends

👥 Top spending customers
