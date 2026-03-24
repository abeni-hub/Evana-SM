# 🛒 Evana SuperMarket Management System (Backend)

A **production-ready backend API** for a **Supermarket / POS (Point of Sale) Management System** built with **Django** and **Django REST Framework**.

This project is designed to manage:

- User authentication & roles
- Product & category management
- Inventory & stock tracking
- Inventory history logging
- Sales / POS transactions
- Profit calculation
- Expense management
- Reports & analytics
- Search, filtering, ordering, and pagination
- Fast POS product search (case-insensitive, instant search after 3 letters)

---

## 🚀 Features

### 👤 User Management
- Authentication system
- Role-based permissions
- Admin and cashier support

### 📦 Product Management
- Create, update, delete, and list products
- Product categories
- Filter products by category
- Search products by name
- Order products by name and price

### 🏬 Inventory Management
- Automatic inventory creation for products
- Add stock
- Remove stock
- Low stock alerts
- Inventory history tracking
- Inventory search and ordering

### 💰 Sales / POS System
- Create sales with multiple items
- Automatic stock deduction after sale
- Subtotal calculation per item
- Total amount calculation
- Profit calculation per item and per sale
- Cashier tracking for each sale

### 🧾 Expense Management
- Record business expenses
- Search and order expenses

### 📊 Reports / Analytics
- Daily sales
- Monthly sales
- Total profit
- Top-selling products
- Low-stock products

### ⚡ Performance Enhancements
- Pagination
- Filtering
- Ordering
- Fast POS search
- Database indexing for optimized loading, filtering, and searching

---

## 🛠️ Tech Stack

- **Python**
- **Django**
- **Django REST Framework**
- **SQLite** (development)
- **MySQL / PostgreSQL** (production-ready)
- **django-filter**
- **Git & GitHub**

---

## 📁 Project Structure

```bash
Evana-SM/
│
├── users/              # Authentication & user roles
├── products/           # Product and category management
├── inventory/          # Inventory and stock history
├── sales/              # Sales, sale items, expenses
├── reports/            # Analytics and reporting APIs
│
├── manage.py
├── requirements.txt
└── README.md
