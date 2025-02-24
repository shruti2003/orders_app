from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from typing import List
from .models import Order  # Fix this line by importing Order properly
from .crud import create_order_in_db, get_all_orders_from_db
from fastapi.staticfiles import StaticFiles
from .database import create_database, create_orders_table
from fastapi.responses import HTMLResponse
from .websockets import send_order_update, websocket_endpoint


# Initialize FastAPI app
app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.add_api_websocket_route("/ws/orders/", websocket_endpoint)



@app.get("/", response_class=HTMLResponse)
async def get_index():
    # Serve index.html from the "static" folder
    with open("app/static/index.html", "r") as f:
        return HTMLResponse(content=f.read())




@app.on_event("startup")
async def startup():
    print("Initializing database...")
    create_database()  # Create the database if it doesn't exist
    create_orders_table()
    print("Database initialized.")

@app.post("/orders/")
async def create_order(order: Order):
    """Create a new order and send a real-time update via WebSocket."""
    print("Received new order:", order)
    
    try:
        print("Attempting to create the order in the database...")
        order_id = await create_order_in_db(order, send_order_update)
        
        print(f"Order created successfully with order_id: {order_id}")
        
        return {"order_id": order_id}
    except Exception as e:
        print(f"Error occurred while creating order: {e}")
        raise HTTPException(status_code=500, detail="Error creating order")


@app.get("/orders/", response_model=List[Order])
def get_orders():
    """Fetch all orders from the database."""
    try:
        orders = get_all_orders_from_db()
        return orders
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching orders")
