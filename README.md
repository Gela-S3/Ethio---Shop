# 🛒 E-commerce Product API

**E-commerce Product API** is a backend project built with **Django** and **Django REST Framework (DRF)**.  
It provides a complete set of APIs for managing products, categories, and users in an online store — including authentication, search, filtering, and pagination.  

This project simulates real-world backend development tasks for e-commerce platforms, focusing on RESTful API design, database management, and secure deployment.

---

## 🚀 Features

### 🧩 Core Features

- **Product Management (CRUD):**
  - Create, Read, Update, and Delete products.
  - Each product includes name, description, price, category, stock quantity, image URL, and creation date.
  - Validation for price, stock quantity, and required fields.

- **User Management (CRUD):**
  - User registration and authentication using Django’s built-in User model.
  - Only authenticated users can manage (create, update, delete) products.

- **Category Management:**
  - Organize products into categories (e.g., Electronics, Clothing, etc.).
  - Filter products by category.

- **Product Search & Filtering:**
  - Search by product name or category.
  - Filter by price range and stock availability.
  - Paginated search results for performance.

- **Authentication & Authorization:**
  - JWT-based authentication via `djangorestframework-simplejwt`.
  - Only authorized users can perform write operations.

- **Pagination & Sorting:**
  - Page-based pagination for product listings.
  - Ordering by price, date created, and stock quantity.

---

## 🧠 Technologies Used

| Category | Technologies |
|-----------|--------------|
| **Backend Framework** | Django 5+, Django REST Framework |
| **Database** | SQLite (default) / PostgreSQL (production) |
| **Authentication** | JWT (via `djangorestframework-simplejwt`) |
| **Filtering & Search** | Django Filter + DRF SearchFilter |
| **Deployment** | Heroku / PythonAnywhere |
| **Environment Management** | Python 3.11+, pip, virtualenv |
| **Server** | Gunicorn (for production) |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Gela-S3/e-commerce-api.git
cd ecommerce-product-api
```

### 2️⃣ Create Virtual Environment

python -m venv venv
source venv/Scripts/activate 


### 3️⃣ Install Dependencies

pip install -r requirements.txt


### 4️⃣ Apply Migrations

python manage.py makemigrations
python manage.py migrate


### 5️⃣ Create Superuser

python manage.py createsuperuser


### 6️⃣ Run Server

python manage.py runserver


### 7️⃣ Access the API

http://127.0.0.1:8000/api/

## API End points

### 1.Register user and Get JWT token:

###     POST http://localhost:8000/api/token/
####        "Content-Type: application/json" 
####        '{"username":"kiyu","password":"kiyukiyu"}'
####            (returns access and refresh tokens)


### 2.	Create Category:

###     POST http://localhost:8000/api/categories/
####        "Content-Type: application/json" 
####        "Authorization: Bearer <ACCESS_TOKEN>" 
####        '{"name":"Electronics","slug":"electronics"}'


### 3.	Create Product:

###     POST http://localhost:8000/api/products/ 
####        "Content-Type: application/json" \
####        "Authorization: Bearer <ACCESS_TOKEN>" \
####        '{"name":"Wireless Headphones","description":"Good sound","price":200,"category_id":1,"stock_quantity":100}'


### 4.	Search products by partial name:

###     GET http://localhost:8000/api/products/?search=headphone&page=1


### 5.	Filter by price range & in stock:

###     GET http://localhost:8000/api/products/?min_price=10&max_price=100&in_stock=true


### 6.	Purchase (reduce stock)
###     POST http://localhost:8000/api/products/5/purchase/
####        "Content-Type: application/json" 
####        "Authorization: Bearer <ACCESS_TOKEN>" 
####        '{"quantity":2}'


## 👨‍💻 Author

### Gelagay Getahun

    📧 gela.sirta3@gmail.com
    🌐 GitHub: github.com/Gela-S3