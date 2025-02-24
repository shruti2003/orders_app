import psycopg2
from fastapi import HTTPException
import os
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file


DB_NAME = "orders_db"
DB_USER = os.getenv("DB_USER")  # Use environment variables
DB_PASSWORD = os.getenv("DB_PASSWORD")  # Use environment variables
DB_HOST = os.getenv("DB_HOST", "db")  # Use 'db' instead of 'localhost'
DB_PORT = "5432"

def get_connection():
    """Connects to the PostgreSQL database."""
    try:
        print("Attempting to connect to the database...")
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Database connection established.")
        return conn
    except psycopg2.OperationalError as e:
        print(f"Error during database connection: {e}")
        raise HTTPException(status_code=500, detail=f"Database connection error: {e}")
    except Exception as e:
        print(f"Unexpected error during database connection: {e}")
        raise HTTPException(status_code=500, detail="Unexpected error occurred while connecting to the database.")


def create_database():
    """Creates the database if it doesn't exist."""
    try:
        conn = psycopg2.connect(
            dbname="postgres",  # Connect to the default 'postgres' database
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")
        exists = cursor.fetchone()
        
        if not exists:
            cursor.execute(f"CREATE DATABASE {DB_NAME}")
            print(f"Database '{DB_NAME}' created.")
        
        cursor.close()
        conn.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating database: {e}")

def create_orders_table():
    """Creates the orders table if it doesn't exist."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id SERIAL PRIMARY KEY,
                symbol VARCHAR(10) NOT NULL,
                quantity INT NOT NULL,
                order_type VARCHAR(10) NOT NULL,
                price DECIMAL(10, 2) NOT NULL
            )
        """)
        
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating table: {e}")
