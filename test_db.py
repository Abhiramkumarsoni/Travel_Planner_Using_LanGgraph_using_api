import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

try:
    with psycopg.connect(DATABASE_URL) as conn:
        result = conn.execute(
            "SELECT current_database(), current_user"
        ).fetchone()

        print("Database connected successfully!")
        print("Database:", result[0])
        print("User:", result[1])

except Exception as e:
    print("Database connection failed!")
    print("Error:", e)