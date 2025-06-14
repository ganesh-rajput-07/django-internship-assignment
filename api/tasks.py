# api/tasks.py
from celery import shared_task

@shared_task
def send_welcome_email(email):
    from django.core.mail import send_mail
    send_mail(
        'Welcome!',
        'Thanks for logging in.',
        'from@example.com',
        [email],
        fail_silently=False,
    )
