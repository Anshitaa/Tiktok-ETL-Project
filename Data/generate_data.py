from faker import Faker
import json, uuid, random
from datetime import datetime, timedelta

fake = Faker()
products = ['Lipstick', 'Serum', 'Eyeliner', 'Foundation', 'Moisturizer']
orders = []

for _ in range(100):
    orders.append({
        "order_id": str(uuid.uuid4()),
        "customer": fake.name(),
        "product": random.choice(products),
        "price": round(random.uniform(10, 100), 2),
        "quantity": random.randint(1, 5),
        "timestamp": (datetime.now() - timedelta(days=random.randint(1, 15))).isoformat()
    })

with open("data/tiktok_orders.json", "w") as f:
    json.dump(orders, f, indent=2)

print("✅ Fake TikTok orders generated.")

