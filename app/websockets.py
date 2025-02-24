# app/websocket.py

import json
from typing import List
from fastapi import WebSocket

active_connections: List[WebSocket] = []

async def websocket_endpoint(websocket: WebSocket):
    """Handle incoming WebSocket connections and send order updates."""
    await websocket.accept()
    
    # Add the connection to the active_connections list
    active_connections.append(websocket)
    
    try:
        while True:
            # Example to listen to any messages from the client if needed
            data = await websocket.receive_text()
            print(f"Received data from client: {data}")
            
    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        # Ensure the connection is removed when the client disconnects
        active_connections.remove(websocket)
        await websocket.close()

async def send_order_update(order):
    """Broadcast the order update to all connected WebSocket clients."""
    message = json.dumps({
        "symbol": order.symbol,
        "quantity": order.quantity,
        "order_type": order.order_type,
        "price": order.price
    })

    # Send the update to each active WebSocket connection
    for connection in active_connections:
        await connection.send_text(message)
