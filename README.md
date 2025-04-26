# 🎟️ Event Ticket Booking System — Full API Documentation

## 📚 Table of Contents
- [📚 Introduction](#-introduction)
- [🏻🏩 Services Overview](#-services-overview)
- [📋 API Endpoint Summary](#-api-endpoint-summary)
- [💑 API Documentation](#-api-documentation)
  - [🔹 event_service](#-event_service)
  - [🔹 order_service](#-order_service)
  - [🔹 user_service](#-user_service)
- [🔗 Inter-Service Communication](#-inter-service-communication)

---

## 📚 Introduction
Dokumentasi ini menjelaskan tentang API sistem Event Ticket Booking yang terdiri dari tiga service:
- **event_service** — Mengelola data event.
- **order_service** — Mengelola data pesanan tiket.
- **user_service** — Mengelola data pengguna.

Service berkomunikasi menggunakan HTTP requests.

---

## 🏻🏩 Services Overview

| Service Name  | Port  | Description                    |
|---------------|-------|---------------------------------|
| user_service  | 5000  | Manajemen data pengguna         |
| event_service | 5001  | Manajemen data event            |
| order_service | 5002  | Manajemen data pemesanan tiket   |

---

## 📋 API Endpoint Summary

| Service        | Method | Endpoint              | Description                          |
|----------------|--------|-----------------------|--------------------------------------|
| event_service  | GET    | /events                | Mengambil semua event                |
| event_service  | GET    | /events/{event_id}     | Mengambil detail event               |
| event_service  | POST   | /events                | Menambahkan event baru               |
| event_service  | PUT    | /events/{event_id}     | Mengupdate event berdasarkan ID      |
| event_service  | DELETE | /events/{event_id}     | Menghapus event berdasarkan ID       |
| order_service  | GET    | /orders                | Mengambil semua order                |
| order_service  | GET    | /orders/{order_id}     | Mengambil detail order               |
| order_service  | POST   | /orders                | Membuat order baru                   |
| user_service   | GET    | /users                 | Mengambil semua pengguna             |
| user_service   | GET    | /users/{user_id}       | Mengambil detail pengguna            |
| user_service   | POST   | /users                 | Menambahkan pengguna baru            |
| user_service   | PUT    | /users/{user_id}       | Mengupdate pengguna berdasarkan ID   |
| user_service   | DELETE | /users/{user_id}       | Menghapus pengguna berdasarkan ID    |

---

# 💑 API Documentation

## 🔹 event_service
**Base URL:** `http://127.0.0.1:5001/events`

### GET /events
- **Deskripsi**: Mengambil daftar semua event.
- **Response 200**:
```json
{
  "1": { "name": "Concert A", "price": 100, "date": "2025-05-01" },
  "2": { "name": "Theater B", "price": 50, "date": "2025-06-15" }
}
```

### GET /events/{event_id}
- **Deskripsi**: Mengambil detail event berdasarkan ID.
- **Parameter**: `event_id` (integer)
- **Response 200**:
```json
{
  "name": "Concert A",
  "price": 100,
  "date": "2025-05-01"
}
```
- **Response 404**: Event tidak ditemukan.

### POST /events
- **Deskripsi**: Menambahkan event baru.
- **Request Body**:
```json
{
  "name": "Concert D",
  "price": 120,
  "date": "2025-08-10"
}
```
- **Response 201**:
```json
{
  "event_id": 3
}
```

### PUT /events/{event_id}
- **Deskripsi**: Mengupdate data event berdasarkan ID.
- **Request Body**:
```json
{
  "name": "Concert A Updated",
  "price": 150,
  "date": "2025-05-10"
}
```
- **Response 200**:
```json
{
  "message": "Event updated successfully!"
}
```
- **Response 404**: Event tidak ditemukan.

### DELETE /events/{event_id}
- **Deskripsi**: Menghapus event berdasarkan ID.
- **Response 200**:
```json
{
  "message": "Event deleted successfully!"
}
```
- **Response 404**: Event tidak ditemukan.

---

## 🔹 order_service
**Base URL:** `http://127.0.0.1:5002/orders`

### GET /orders
- **Deskripsi**: Mengambil semua data order.
- **Response 200**:
```json
[
  {
    "order_id": 1,
    "user_id": 1,
    "user_name": "Alice Smith",
    "event_id": 1,
    "event_name": "Concert A",
    "quantity": 2,
    "total": 200,
    "order_date": "2025-04-26"
  }
]
```

### GET /orders/{order_id}
- **Deskripsi**: Mengambil detail order berdasarkan ID.
- **Parameter**: `order_id` (integer)
- **Response 200**:
```json
{
  "order_id": 1,
  "user_id": 1,
  "user_name": "Alice Smith",
  "event_id": 1,
  "event_name": "Concert A",
  "quantity": 2,
  "total": 200,
  "order_date": "2025-04-26"
}
```
- **Response 404**: Order tidak ditemukan.

### POST /orders
- **Deskripsi**: Membuat order baru.
- **Request Body**:
```json
{
  "user_id": 1,
  "event_id": 1,
  "quantity": 2,
  "total": 200
}
```
- **Response 201**:
```json
{
  "message": "Order created successfully!",
  "order_id": 2
}
```

---

## 🔹 user_service
**Base URL:** `http://127.0.0.1:5000/users`

### GET /users
- **Deskripsi**: Mengambil daftar semua pengguna.
- **Response 200**:
```json
{
  "1": { "name": "Alice Smith", "email": "alice@gmail.com" },
  "2": { "name": "Bob Johnson", "email": "bob@gmail.com" }
}
```

### GET /users/{user_id}
- **Deskripsi**: Mengambil detail pengguna berdasarkan ID.
- **Parameter**: `user_id` (integer)
- **Response 200**:
```json
{
  "name": "Alice Smith",
  "email": "alice@gmail.com"
}
```
- **Response 404**: User tidak ditemukan.

### POST /users
- **Deskripsi**: Menambahkan pengguna baru.
- **Request Body**:
```json
{
  "name": "Charlie Brown",
  "email": "charlie@gmail.com"
}
```
- **Response 201**:
```json
{
  "user_id": 3
}
```

### PUT /users/{user_id}
- **Deskripsi**: Mengupdate data pengguna berdasarkan ID.
- **Request Body**:
```json
{
  "name": "Alice Smith Updated",
  "email": "alice_updated@gmail.com"
}
```
- **Response 200**:
```json
{
  "message": "User updated successfully!"
}
```
- **Response 404**: User tidak ditemukan.

### DELETE /users/{user_id}
- **Deskripsi**: Menghapus pengguna berdasarkan ID.
- **Response 200**:
```json
{
  "message": "User deleted successfully!"
}
```
- **Response 404**: User tidak ditemukan.

---

# 🔗 Inter-Service Communication

## 🔸 Order Service ➡️ Event Service
- **Purpose**: Mengambil detail event untuk menghitung total harga tiket.
- **Request**:
```
GET http://127.0.0.1:5001/events/{event_id}
```
- **Expected Response**:
```json
{
  "name": "Concert A",
  "price": 100,
  "date": "2025-05-01"
}
```

## 🔸 Order Service ➡️ User Service
- **Purpose**: Mengambil detail user untuk mencatat pemilik order.
- **Request**:
```
GET http://127.0.0.1:5000/users/{user_id}
```
- **Expected Response**:
```json
{
  "name": "Alice Smith",
  "email": "alice@gmail.com"
}
