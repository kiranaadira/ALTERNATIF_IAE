### <a name="_5d08dtim7m0w"></a>**Laporan Dokumentasi API dan Komunikasi Antar Layanan**
#### <a name="_1czossiyd853"></a>**Laporan Dokumentasi API**
1. **Pendahuluan**
   Dokumentasi ini menjelaskan API yang digunakan dalam sistem Event Ticket Booking, yang terdiri dari tiga layanan utama: event\_service, order\_service, dan user\_service. Setiap layanan menyediakan fungsionalitas tertentu yang saling berinteraksi untuk memastikan kelancaran proses pemesanan tiket.

1. **Struktur API Layanan**
1. **event\_service (Port: 5001)**
   Menyediakan data tentang event yang tersedia untuk pemesanan.
1. **order\_service (Port: 5002)**
   Menyediakan data tentang pemesanan yang dilakukan oleh pengguna dan memproses order baru.
1. **user\_service (Port: 5000)**
   Menyediakan data pengguna yang melakukan pemesanan.
1. #### <a name="_hv1yc0hk95jf"></a>**Dokumentasi API untuk event\_service**
**Base URL**: http://127.0.0.1:5001/events
1. ##### <a name="_3psvsxbindmd"></a>**GET /events**
- **Deskripsi**: Mengambil daftar semua event yang tersedia.
- **Metode**: GET
- **Response**:
- **Status 200**: Mengembalikan objek JSON yang berisi daftar semua event.

  **Body Response**:
  ` `{

  `  `"1": {

  `    `"name": "Concert A",

  `    `"price": 100,

  `    `"date": "2025-05-01"

  `  `},

  `  `"2": {

  `    `"name": "Theater B",

  `    `"price": 50,

  `    `"date": "2025-06-15"

  `  `},

  `  `"3": {

  `    `"name": "Festival C",

  `    `"price": 75,

  `    `"date": "2025-07-20"

  `  `}

  }
1. ##### <a name="_yg10ohysso45"></a>**GET /events/{event\_id}**
- **Deskripsi**: Mengambil detail event berdasarkan ID event.
- **Metode**: GET
- **Parameter**:
- event\_id (int): ID event yang akan diambil.
- **Response**:
- **Status 200**: Mengembalikan detail event berdasarkan event\_id.
- **Status 404**: Jika event tidak ditemukan.

  **Body Response**:
  ` `{

  `  `"name": "Concert A",

  `  `"price": 100,

  `  `"date": "2025-05-01"

  }
1. ##### <a name="_1r0nvsetxslk"></a>**POST /events**
- **Deskripsi**: Menambahkan event baru ke dalam sistem.
- **Metode**: POST

  **Body Request**:
  ` `{

`  `"name": "Concert A",

`  `"price": 100,

`  `"date": "2025-05-01"

}



- **Response**:
- **Status 201**: Event baru berhasil ditambahkan.

  **Body Response**:
  ` `{

  `  `"event\_id": 4

  }

1. ##### <a name="_ujz023wef9w1"></a>**DELETE /events/{event\_id}**
- **Deskripsi**: Menghapus event berdasarkan event\_id.
- **Metode**: DELETE
- **Parameter**:
- event\_id (int): ID event yang akan dihapus.
- **Response**:
- **Status 200**: Event berhasil dihapus.
- **Status 404**: Event tidak ditemukan.

  **Body Response**:

  ` `{

  `  `"message": "Event deleted successfully!"

  }
1. #### <a name="_h8e5658ol4hx"></a>**Dokumentasi API untuk order\_service**
**Base URL**: http://127.0.0.1:5002/orders
##### <a name="_1vtwmwudrvl4"></a>**1. GET /orders**
- **Deskripsi**: Mengambil daftar semua order yang dilakukan oleh pengguna.
- **Metode**: GET
- **Response**:
- **Status 200**: Mengembalikan daftar order dengan detail pengguna dan event terkait.

  **Body Response**:

  ` `[

  `  `{

  `    `"order\_id": 1,

  `    `"user\_id": 1,

  `    `"user\_name": "Alice Smith",

  `    `"event\_id": 1,

  `    `"event\_name": "Concert A",

  `    `"quantity": 2,

  `    `"total": 200.00,

  `    `"order\_date": "2025-04-26"

  `  `},

  `  `{

  `    `"order\_id": 2,

  `    `"user\_id": 2,

  `    `"user\_name": "Bob Johnson",

  `    `"event\_id": 2,

  `    `"event\_name": "Theater B",

  `    `"quantity": 1,

  `    `"total": 50.00,

  `    `"order\_date": "2025-04-26"

  `  `}

  ]
##### <a name="_a1q3tk76yjij"></a>**2. POST /orders**
- **Deskripsi**: Membuat order baru.
- **Metode**: POST

  **Body Request**:
  ` `{

  `  `"user\_id": 1,

  `  `"event\_id": 1,

  `  `"quantity": 2,

  `  `"total": 200.00

  }

- **Response**:
- **Status 201**: Mengembalikan ID order yang baru dibuat.

  **Body Response**
  ` `{

  `  `"message": "Order created successfully!",

  `  `"order\_id": 4

  }
1. #### <a name="_rnrwkawku3tl"></a>**Dokumentasi API untuk user\_service**
**Base URL**: http://127.0.0.1:5000/users
##### <a name="_3z1e1rzi858y"></a>**1. GET /users**
- **Deskripsi**: Mengambil daftar semua pengguna yang terdaftar dalam sistem.
- **Metode**: GET
- **Response**:
- **Status 200**: Mengembalikan daftar semua pengguna.

  **Body Response**:
  ` `{

  `  `"1": {

  `    `"name": "Alice Smith",

  `    `"email": "alice@gmail.com"

  `  `},

  `  `"2": {

  `    `"name": "Bob Johnson",

  `    `"email": "bob@gmail.com"

  `  `}

  }
##### <a name="_v2ue4e5avukq"></a>**2. GET /users/{user\_id}**
- **Deskripsi**: Mengambil detail pengguna berdasarkan user\_id.
- **Metode**: GET
- **Parameter**:
- user\_id (int): ID pengguna yang akan diambil.
- **Response**:
- **Status 200**: Mengembalikan detail pengguna berdasarkan user\_id.
- **Status 404**: Jika pengguna tidak ditemukan.

  **Body Response**:
  ` `{

  `  `"name": "Alice Smith",

  `  `"email": "alice@gmail.com"

  }
##### <a name="_f7n84wmpvn1a"></a>**3. POST /users**
- **Deskripsi**: Menambahkan pengguna baru ke dalam sistem.
- **Metode**: POST

  **Body Request**:
  ` `{

  `  `"name": "Alice Smith",

  `  `"email": "alice@gmail.com"

  }

- **Response**:
- **Status 201**: Pengguna baru berhasil ditambahkan.

  **Body Response**:
  ` `{

  `  `"user\_id": 4

  }

1. **Komunikasi Antar Layanan**

   Dalam sistem ini, komunikasi antar layanan dilakukan melalui HTTP Request. Setiap layanan memiliki endpoint yang digunakan oleh layanan lain untuk mengambil atau mengirimkan data.

1. **Order Service & Event Service**

   Layanan order\_service berkomunikasi dengan event\_service untuk mengambil detail acara berdasarkan event\_id untuk pesanan tertentu. Untuk setiap pesanan, order\_service mengirimkan permintaan GET ke /events/<event\_id> untuk mendapatkan detail acara.

   **Contoh Permintaan:**

   GET <http://127.0.0.1:5001/events/1>

   **Contoh Respons:**

   {

   `  `"name": "Konser A",

   `  `"price": 100,

   `  `"date": "2025-05-01"

   }



1. **Order Service & User Service**

   Layanan order\_service juga berkomunikasi dengan user\_service untuk mengambil detail pengguna berdasarkan user\_id untuk pesanan tertentu. Untuk setiap pesanan, order\_service mengirimkan permintaan GET ke /users/<user\_id> untuk mendapatkan nama pengguna.

   **Contoh Permintaan:**

   GET <http://127.0.0.1:5000/users/1>

   **Contoh Respons:**

   {

   `  `"name": "Alice Smith",

   `  `"email": "alice@gmail.com"

   }


