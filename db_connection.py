import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE

def get_connection():
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    return conn

# TEST
if __name__ == "__main__":
    conn = get_connection()
    print("Connected to MySQL successfully!")
    conn.close()