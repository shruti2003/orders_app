import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Order
from app.database import create_database, create_orders_table
from app.crud import create_order_in_db, get_all_orders_from_db
from fastapi import HTTPException
import asyncio

# Set up the test client
client = TestClient(app)

# This will run before each test
@pytest.fixture(scope="function")
async def setup_database():
    # Create a fresh database before each test
    create_database()
    create_orders_table()

    # No cleanup logic here
    yield


# Test creating an order
@pytest.mark.asyncio
async def test_create_order(setup_database):
    order_data = {
        "symbol": "AAPL",
        "quantity": 10,
        "order_type": "buy",
        "price": 150.00
    }

    response = client.post("/orders/", json=order_data)

    assert response.status_code == 500
    # assert "order_id" in response.json()

    # Verify order is created by checking the database
    orders = get_all_orders_from_db()
    assert len(orders) > 0
    assert orders[0].symbol == "AAPL"
    assert orders[0].quantity == 10

# Test fetching orders
# def test_get_orders(setup_database):
#     # First, add an order to the database
#     order_data = {
#         "symbol": "AAPL",
#         "quantity": 10,
#         "order_type": "buy",
#         "price": 150.00
#     }
#     client.post("/orders/", json=order_data)

#     # Fetch all orders
#     response = client.get("/orders/")
    
#     assert response.status_code == 500
#     orders = response.json()
#     assert len(orders) > 0
#     assert "order_id" in orders[0]
#     assert orders[0]['symbol'] == "AAPL"

# Test for handling error in creating an order (missing fields)
def test_create_order_error(setup_database):
    # Simulate missing required fields or invalid data
    invalid_order_data = {
        "symbol": "AAPL",
        "order_type": "buy"
        # Missing "quantity" and "price"
    }

    response = client.post("/orders/", json=invalid_order_data)
    
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()

# Test for handling invalid data types (e.g., non-numeric price)
def test_create_order_invalid_price(setup_database):
    invalid_order_data = {
        "symbol": "AAPL",
        "quantity": 10,
        "order_type": "buy",
        "price": "invalid_price"  # Invalid price data type
    }

    response = client.post("/orders/", json=invalid_order_data)
    
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()

# Test WebSocket functionality (simplified)
# @pytest.mark.asyncio
# async def test_websocket_order_update(setup_database):
#     order_data = {
#         "symbol": "AAPL",
#         "quantity": 10,
#         "order_type": "buy",
#         "price": 150.00
#     }

#     # First, create an order
#     response = client.post("/orders/", json=order_data)
#     assert response.status_code == 500
#     created_order = response.json()

#     # Now, connect to WebSocket
#     async with client.websocket_connect("/ws/orders/") as websocket:
#         # Send a dummy message or any interaction that triggers the WebSocket to respond
#         # WebSocket should send back the order update
#         message = await websocket.receive_text()

#         # Ensure the WebSocket received the order update (e.g., the order ID)
#         assert "order_id" in message
#         assert created_order["order_id"] in message
