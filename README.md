# 📚 Library Management System API

This is a **Library Management System API** built using **Django** and **Django REST Framework (DRF)**.  
It allows users to **borrow books**, **earn points**, and manage library resources efficiently.

---

## 🚀 Features

- 🧾 User registration and authentication (using DRF)
- 📚 Add, view, update, and delete books
- 🔄 Borrow and return books
- 💰 Earn points for borrowing and returning on time
- ❌ Deduct points for late returns
- 🧠 API endpoints for managing books, users, and transactions

---

## 💡 How It Works

1. A user can **borrow a book** through the API.
2. When a book is borrowed:
   - The user’s **borrowed book count increases**.
   - The book’s **availability changes to false**.
3. When the book is returned:
   - The book’s availability becomes **true** again.
   - The user **earns points** for returning it on time.
   - If the book is late, **points are deducted**.
4. Users can check their total points anytime through their profile endpoint.

---

## 🔗 API Endpoints

### 📘 Books
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/api/books/` | List all books |
| POST | `/api/books/` | Add a new book |
| GET | `/api/books/{id}/` | View a specific book |
| PUT | `/api/books/{id}/` | Update a book |
| DELETE | `/api/books/{id}/` | Delete a book |

### 👤 Users
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/api/users/register/` | Register a new user |
| POST | `/api/users/login/` | Login and get token |
| GET | `/api/users/profile/` | View user details (including points) |

### 🔄 Borrowing
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/api/borrow/{book_id}/` | Borrow a book |
| POST | `/api/return/{book_id}/` | Return a borrowed book |
| GET | `/api/transactions/` | View borrow/return history |

---

## 🧠 Points System

| Action | Points |
|--------|--------|
| Borrow a book | +5 |
| Return on time | +10 |
| Late return | −5 |

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Porshh100/Library-management-system-API.git
