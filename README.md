# ALX Backend Security

## Task 0: Basic IP Logging Middleware

This project implements middleware to log the IP address, timestamp, and path of every incoming request.

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Start the development server:
```bash
python manage.py runserver
```

### Features

- **IP Tracking Middleware**: Automatically logs all incoming requests
- **RequestLog Model**: Stores IP address, timestamp, and request path
- **Admin Interface**: View logged requests in Django admin