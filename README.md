# BON Rewards API 🎁

**BON Rewards** is a backend system built with **FastAPI** that simulates a credit card rewards program.
Users earn **mock gift card rewards** (like “\$10 Amazon Gift Card”) when they consistently pay their **last 3 bills on time**.

---

## 🚀 Features

* 👤 Create and manage users
* 🧾 Create bills for users
* 💳 Pay bills and auto-generate rewards if last 3 bills were on time
* 🎁 Fetch all rewards for a user
* 🌐 Works locally and deploys easily on **Render** with PostgreSQL

---

## 🛠 Tech Stack

* **Backend:** FastAPI
* **Database:** PostgreSQL (local or Render-managed)
* **ORM:** SQLAlchemy
* **Validation:** Pydantic
* **Deployment:** Render-ready

---

## ⚡ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone <repo_url>
cd Credit_Reward
```

### 2️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure database URL

#### Local:

```bash
export DATABASE_URL="postgresql://<user>:<password>@<host>:5432/<dbname>"
```

#### Render:

Set `DATABASE_URL` inside **Render Dashboard → Environment Variables**.

---

## ▶️ Running the API

```bash
uvicorn app.main:app --reload
```

Visit interactive docs: 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📌 API Endpoints

### 👤 Users

**Create a user**
`POST /users/`

```json
{
  "name": "Ritik",
  "email": "test@example.com"
}
```

**Response**

```json
{
  "user_id": 1,
  "name": "Ritik",
  "email": "test@example.com"
}
```

---

### 🧾 Bills

**Create a bill**
`POST /bills/`

```json
{
  "user_id": 1,
  "due_date": "2025-09-15"
}
```

**Response**

```json
{
  "bill_id": 1,
  "user_id": 1,
  "due_date": "2025-09-15",
  "payment_date": null
}
```

**Pay a bill (and maybe earn a reward)**
`POST /bills/pay/`

```json
{
  "bill_id": 1,
  "payment_date": "2025-09-15"
}
```

**Response (with reward)**

```json
{
  "bill_id": 1,
  "user_id": 1,
  "due_date": "2025-09-15",
  "payment_date": "2025-09-15",
  "reward": {
    "reward_id": 1,
    "user_id": 1,
    "reward_name": "$10 Amazon Gift Card"
  }
}
```

---

### 🎁 Rewards

**Get all rewards for a user**
`GET /rewards/{user_id}`
**Response**

```json
[
  {
    "reward_id": 1,
    "user_id": 1,
    "reward_name": "$10 Amazon Gift Card"
  }
]
```

---

## ✅ Notes

* Rewards are granted **only if the last 3 bills were paid on or before the due date**.
* Emails are **unique** – trying to create a user with an existing email will fail.
* Ready for **production deployment on Render** with PostgreSQL.
