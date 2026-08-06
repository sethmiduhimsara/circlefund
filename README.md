# circlefund


# CircleFund - ROSCA Management System

A full-stack mobile application for managing a **Rotating Savings and Credit Association (ROSCA)**, developed as a technical assessment.

## Overview

CircleFund enables users to create and manage savings circles where members contribute regularly and receive payouts in a rotating order.

The project consists of:

- **Backend:** Django + Django REST Framework
- **Authentication:** JWT (Simple JWT)
- **Database:** SQLite
- **Frontend:** React Native (Expo)

---

# Features

## Authentication

- User Registration
- JWT Login
- Protected API Endpoints

## Circle Management

- Create a Circle
- Join a Circle using an Invite Code
- Maximum of 4 Members per Circle
- Automatic Rotation Position Assignment

## Round Management

- Automatically creates the first round when a circle is created
- Tracks round status (OPEN / CLOSED)

## Contributions

- Members contribute to the active round
- Prevents duplicate contributions

## Payout Management

- Admin approves payouts
- Uses database transactions (`transaction.atomic`)
- Uses row locking (`select_for_update`)
- Automatically closes completed rounds
- Automatically creates the next round
- Verifies all members contributed before payout approval

---

# Tech Stack

## Backend

- Python
- Django
- Django REST Framework
- Simple JWT

## Frontend

- React Native
- Expo
- Axios
- Expo Router

---

# Project Structure

```
backend/
│
├── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── config/
│   ├── settings.py
│   └── urls.py
│
└── manage.py


circlefund-mobile/
│
├── src/
│   ├── app/
│   ├── services/
│   ├── components/
│   └── navigation/
│
└── package.json
```

---

# Installation

## Backend

### Clone Repository

```bash
git clone <repository-url>
cd backend
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Backend URL

```
http://127.0.0.1:8000/
```

---

# Frontend

Navigate to the mobile project.

```bash
cd circlefund-mobile
```

Install dependencies.

```bash
npm install
```

Start Expo.

```bash
npx expo start
```

---

# API Endpoints

## Authentication

### Register

```
POST /api/register/
```

### Login

```
POST /api/login/
```

### Refresh Token

```
POST /api/token/refresh/
```

---

## Circle

### Create Circle

```
POST /api/circles/
```

### Join Circle

```
POST /api/circles/join/
```

---

## Contribution

### Contribute

```
POST /api/rounds/<round_id>/contribute/
```

---

## Payout

### Approve Payout

```
POST /api/rounds/<round_id>/approve/
```

---

# Database Models

- User
- Circle
- CircleMember
- Round
- Contribution
- Payout

---

# Business Rules

- Maximum of 4 members per circle.
- Circle creator becomes the administrator.
- Members join using an invite code.
- Rotation order is assigned automatically.
- Each member can contribute only once per round.
- Payout approval is restricted to the circle administrator.
- A payout cannot be approved until every member has contributed.
- Approval closes the current round and creates the next round automatically.

---

# Security

- JWT Authentication
- Protected API endpoints
- Database transactions
- Row-level locking for payout approval

---

# Future Improvements

- Notifications
- Penalty management
- Payment gateway integration
- Dashboard analytics
- Push notifications
- Automated testing
- Docker deployment

---

# Author

Developed as a technical assessment for the PayBay Backend Developer assignment.
