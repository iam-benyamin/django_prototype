# django_prototype
Prototype Features

## Instruction
python manage.py migrate
python manage.py init_pod


## Challenges
1. after authentication, <http://127.0.0.1:8000/pod/description> should return the description of account owner' company.
2. <http://127.0.0.1:8000/pod/update> should run a background task in a celery worker.
