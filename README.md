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
- AWS Account with EC2 access
- GitHub Account

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/order-management-api.git
cd order-management-api


# Order Management API

This is a simple backend service built using FastAPI to manage orders. The service provides REST API endpoints for creating orders, fetching orders, and also supports real-time order updates using WebSocket.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [POST /orders/](#post-orders)
  - [GET /orders/](#get-orders)
  - [WebSocket /ws/orders/](#websocket-wsorders)
- [Running the Application](#running-the-application)
- [Docker Setup](#docker-setup)
- [CI/CD Setup](#cicd-setup)
- [Development Guidelines](#development-guidelines)
- [Contributing](#contributing)
- [License](#license)

## Overview

This application is designed to manage orders for a store or trading platform. It allows users to:

1. Create a new order by providing details such as product name, quantity, and price.
2. Fetch a list of all orders from the database.
3. Receive real-time updates about order status via WebSocket.

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-username/order-management-api.git
cd order-management-api
pip install -r requirements.txt
