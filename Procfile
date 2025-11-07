web: gunicorn --bind 0.0.0.0:$PORT wsgi:application
worker: celery -A celery_app worker --loglevel=info
beat: celery -A celery_app beat --loglevel=info