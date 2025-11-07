# ALX Backend Security

A comprehensive Django application for IP tracking, security monitoring, and anomaly detection with REST API and Swagger documentation.

## Features

- **IP Tracking Middleware**: Logs all incoming requests with geolocation
- **IP Blacklisting**: Block malicious IPs with 403 responses
- **Rate Limiting**: 10 req/min (authenticated), 5 req/min (anonymous)
- **Anomaly Detection**: Celery tasks flag suspicious activity
- **REST API**: Full CRUD operations with DRF
- **Swagger Documentation**: Interactive API documentation
- **Production Ready**: Configured for cloud deployment

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Collect static files:
```bash
python manage.py collectstatic
```

4. Start the development server:
```bash
python manage.py runserver
```

5. Start Celery worker (separate terminal):
```bash
celery -A celery_app worker --loglevel=info
```

6. Start Celery beat (separate terminal):
```bash
celery -A celery_app beat --loglevel=info
```

## API Endpoints

- **Swagger UI**: `/swagger/`
- **API Status**: `/api/status/`
- **Request Logs**: `/api/request-logs/`
- **Blocked IPs**: `/api/blocked-ips/`
- **Suspicious IPs**: `/api/suspicious-ips/`
- **Login**: `/login/`

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

## Management Commands

- Block IP: `python manage.py block_ip <ip_address>`
- Detect Anomalies: `python manage.py detect_anomalies`