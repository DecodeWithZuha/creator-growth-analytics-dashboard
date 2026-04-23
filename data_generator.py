from db_connection import get_connection
import random
from datetime import date, timedelta

conn = get_connection()
cursor = conn.cursor()

# countries list
countries = [
    "Pakistan", "India", "Bangladesh", "Sri Lanka", "Nepal",
    "UK", "USA", "Canada", "Australia", "Germany",
    "France", "Italy", "Spain", "Netherlands", "Turkey",
    "UAE", "Saudi Arabia", "Qatar", "Kuwait", "Oman",
    "Malaysia", "Indonesia", "Philippines", "Singapore", "South Africa",
    "Nigeria", "Brazil", "Mexico"
]

devices = ["Android", "iOS", "Web"]

query = "INSERT INTO users (signup_date, country, device) VALUES (%s, %s, %s)"

# April 2026 range setup
start_date = date(2026, 4, 1)
end_days = 30  # April has 30 days

# generating 1000 users
for i in range(1000):

    signup_date = start_date + timedelta(
        days=random.randint(0, end_days - 1)
    )

    country = random.choice(countries)
    device = random.choice(devices)

    cursor.execute(query, (signup_date, country, device))


event_query = """
INSERT INTO events (user_id, campaign_id, event_type, event_time)
VALUES (%s, %s, %s, %s)
"""

event_types = ["visit", "signup", "app_open", "purchase"]

for user_id in range(1, 1001):  # because you now have 100 users

    # each user gets 1–4 events
    event_count = random.randint(1, 4)

    base_date = date(2026, 4, 1)

    for i in range(event_count):

        event_type = random.choices(
            event_types,
            weights=[50, 30, 15, 5]  # realistic funnel drop
        )[0]

        event_time = base_date + timedelta(days=random.randint(0, 29))

        campaign_id = random.randint(1, 4)  # assuming 4 campaigns

        cursor.execute(
            event_query,
            (user_id, campaign_id, event_type, event_time)
        )

conn.commit()
cursor.close()
conn.close()