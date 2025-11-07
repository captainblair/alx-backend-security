# Deployment Guide

## Prerequisites
- Redis server for Celery broker
- Python 3.11+
- Git repository

## Environment Variables
Set these environment variables on your hosting platform:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

## Deployment Steps

### 1. Render.com Deployment
1. Connect your GitHub repository
2. Set environment variables in Render dashboard
3. Deploy web service with build command: `pip install -r requirements.txt`
4. Start command: `gunicorn wsgi:application`
5. Add Redis service for Celery
6. Deploy worker service with start command: `celery -A celery_app worker --loglevel=info`

### 2. PythonAnywhere Deployment
1. Upload code to PythonAnywhere
2. Set up virtual environment: `python -m venv venv`
3. Install requirements: `pip install -r requirements.txt`
4. Configure WSGI file
5. Set environment variables in .env file
6. Run migrations: `python manage.py migrate`
7. Collect static files: `python manage.py collectstatic`

## API Documentation
- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

## Testing Endpoints
- API Status: `/api/status/`
- Request Logs: `/api/request-logs/`
- Blocked IPs: `/api/blocked-ips/`
- Suspicious IPs: `/api/suspicious-ips/`