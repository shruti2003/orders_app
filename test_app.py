import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Order  # Make sure this import path is correct
from app.database import create_database, create_orders_table
from app.crud import create_order_in_db, get_all_orders_from_db

# Set up the test client
client = TestClient(app)

# This will run before each test
@pytest.fixture(scope="function")
def setup_database():
    # Create a fresh database before each test
    create_database()
    create_orders_table()

    yield

    # After each test, you can clean up the database if needed
    # For now, assuming orders are created in a test database that is isolated

# Test creating an order
def test_create_order(setup_database):
    order_data = {
        "customer_name": "Test Customer",
        "item": "Laptop",
        "quantity": 1,
        "price": 1000.00
    }

    response = client.post("/orders/", json=order_data)

    assert response.status_code == 200
    assert "order_id" in response.json()

# Test fetching orders
def test_get_orders(setup_database):
    # First, add an order to the database
    order_data = {
        "customer_name": "Test Customer",
        "item": "Laptop",
        "quantity": 1,
        "price": 1000.00
    }
    client.post("/orders/", json=order_data)
    
    response = client.get("/orders/")
    
    assert response.status_code == 200
    orders = response.json()
    assert len(orders) > 0  # Ensure the order list isn't empty
    assert "order_id" in orders[0]



# Test for handling error in creating an order
def test_create_order_error(setup_database):
    # Simulate missing required fields or invalid data
    invalid_order_data = {
        "customer_name": "Test Customer",
        "item": "Laptop"
        # Missing "quantity" and "price"
    }

    response = client.post("/orders/", json=invalid_order_data)
    
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()
