# Backend Service for Order Management API

## Overview

This project is a simple backend service that exposes REST APIs to manage trade orders. It uses **FastAPI** as the web framework and supports **WebSocket** for real-time updates. The service supports basic CRUD operations on orders, stores data in a **PostgreSQL** database, and provides a **Dockerized** deployment on **AWS EC2**. The application also implements **CI/CD** using **GitHub Actions** to automate testing, containerization, and deployment.

## Features

- **REST API Endpoints**:
  - `GET /orders/`: Fetches all submitted orders.
  - `POST /orders/`: Accepts a new order and stores it in the database.
  
- **WebSocket**:
  - `GET /ws/orders/`: Real-time updates for order status.

- **Database**: 
  - PostgreSQL to store order details.
  
- **Deployment**:
  - Dockerized application.
  - Deployed on an AWS EC2 instance.

- **CI/CD Pipeline**:
  - GitHub Actions to automate testing, building Docker images, and deployment.

---

## Technologies Used

- **FastAPI**: Python web framework for building APIs.
- **WebSocket**: For real-time order updates.
- **PostgreSQL**: Database to store order details.
- **Docker**: Containerization of the application.
- **AWS EC2**: Cloud hosting for the containerized application.
- **GitHub Actions**: CI/CD automation.

---

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Docker
- Defined in requirements.txt
