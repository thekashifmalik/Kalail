web: python manage.py run_gunicorn --workers=9 --bind=0.0.0.0:$PORT
worker_beat: python manage.py celery worker -E -B --loglevel=INFO
celerycam: python manage.py celerycam