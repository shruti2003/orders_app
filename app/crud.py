from .database import get_connection
from .models import Order

# app/crud.py

from .websockets import send_order_update  # Import the WebSocket broadcast function

# app/crud.py

async def create_order_in_db(order: Order, send_order_update):
    """Insert a new order into the database and return its order ID."""
    print("Attempting to create a new order in the database...")
    
    try:
        conn = get_connection()
        cursor = conn.cursor()

        print("Database connection established. Inserting order into the database...")
        
        cursor.execute("""
            INSERT INTO orders (symbol, quantity, order_type, price)
            VALUES (%s, %s, %s, %s)
            RETURNING order_id;
        """, (order.symbol, order.quantity, order.order_type, order.price))

        order_id = cursor.fetchone()[0]
        print(f"Order inserted successfully with order ID: {order_id}")

        conn.commit()
        cursor.close()
        conn.close()
        
        # Fetch the newly created order
        created_order = Order(
            symbol=order.symbol,
            quantity=order.quantity,
            order_type=order.order_type,
            price=order.price
        )

        print("Order object created, now sending update to WebSocket...")

        # Import inside the function to avoid circular import issues
        from .websockets import send_order_update

        # Send the order update via WebSocket
        await send_order_update(created_order)

        print("Order update sent via WebSocket.")
        
        return order_id
    except Exception as e:
        print(f"An error occurred while creating the order: {e}")
        raise



def get_all_orders_from_db():
    """Fetch all orders from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT order_id, symbol, quantity, order_type, price FROM orders")
    rows = cursor.fetchall()

    orders = []
    for row in rows:
        orders.append(Order(
            symbol=row[1],
            quantity=row[2],
            order_type=row[3],
            price=row[4]
        ))

    cursor.close()
    conn.close()
    return orders
