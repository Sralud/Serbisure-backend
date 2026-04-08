# SerbiSure Backend

A Django REST Framework backend for **SerbiSure** — a home services platform connecting **Homeowners** with **Service Workers**.

---

## About SerbiSure

SerbiSure allows homeowners to browse and book local home services (plumbing, electrical, cleaning, etc.) and service workers to manage their profiles and accept jobs. This backend provides a RESTful API that supports the web and mobile frontends.

### User Roles

| Role | Description |
|---|---|
| **Homeowner** | Browses services, creates bookings, manages their profile |
| **Service Worker** | Offers services, receives bookings, manages their worker profile |

---

## Key Features

- User registration and login (with token-based authentication)
- Service listings (browse available home services)
- Booking system (homeowners can book services)
- Worker profiles (bio, skills, ratings)
- Role-based access control

---

## Tech Stack

- **Python** 3.x
- **Django** 6.x
- **Django REST Framework** (DRF)
- **SQLite** (local development)

---

## Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/serbisure-backend.git
cd serbisure-backend
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies
```bash
pip install django djangorestframework
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (for admin access)
```bash
python manage.py createsuperuser
```

### 6. Start the development server
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## API Endpoints

| Endpoint | Method | Description | Auth Required |
|---|---|---|---|
| `/api/auth/register/` | POST | Register a new user | No |
| `/api/auth/login/` | POST | Login and receive token | No |
| `/api/services/` | GET | List all services | No |
| `/api/bookings/` | GET, POST | List/create bookings | Yes |
| `/api/profile/` | GET | View logged-in user profile | Yes |

---

## Admin Panel

Visit `http://127.0.0.1:8000/admin/` and log in with your superuser credentials to manage users, services, and bookings.
