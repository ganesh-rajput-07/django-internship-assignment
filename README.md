# Django Internship Assignment

## Project Overview

This is a Django REST Framework-based backend project for internship evaluation. It demonstrates:

* Public and protected APIs
* Token-based authentication
* Celery integration with Redis for background tasks
* Telegram bot integration to collect Telegram usernames

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/django-internship-assignment.git
cd django-internship-assignment
```

### 2. Create Virtual Environment

```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For Linux/Mac:
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Create `.env` File

The `.env` file should not be pushed to GitHub (keep it secret). Add this file to `.gitignore`.

#### Example `.env` File:

```env
SECRET_KEY=your_django_secret_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run Server

```bash
python manage.py runserver
```

### 8. Start Redis Server

```bash
redis-server
```

### 9. Start Celery Worker

```bash
celery -A django_internship worker --loglevel=info
```

### 10. Run Telegram Bot

```bash
python manage.py shell
from api.bot import run_bot
run_bot()
```

---

## API Endpoints

| Endpoint        | Method | Authentication |
| --------------- | ------ | -------------- |
| /api/public/    | GET    | No             |
| /api/protected/ | GET    | Token          |
| /api/login/     | POST   | No             |

### Example Login Request (POST)

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

### Example Authorization Header for Protected API

```http
Authorization: Token your_token_here
```

---

## Telegram Bot

* Search your bot on Telegram.
* Send `/start` to the bot.
* The bot will reply with a welcome message and your Telegram username will be stored in the Django database.

---

## Environment Variables

| Variable             | Purpose            |
| -------------------- | ------------------ |
| SECRET\_KEY          | Django secret key  |
| TELEGRAM\_BOT\_TOKEN | Telegram bot token |

---

## Notes

* The `.env` file should be added to `.gitignore` to keep secrets safe.
* Push only the required source code to GitHub.
* Deployment is not required for submission.

---

## Submission

Submit the GitHub repository URL only.
