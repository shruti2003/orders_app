# app/__init__.py

# Import the FastAPI app instance from main.py
from .main import app

# Optionally, import any shared components that you want to expose at the package level
# from .database import get_db
# from .models import Item  # Example of a model you may want to expose
# from .crud import create_item, get_items  # Example of exposing some CRUD functions

# This can also include versioning information
__version__ = '1.0.0'

# You could set up additional initialization logic if needed
def init_app():
    print("App initialized.")
