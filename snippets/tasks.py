from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_welcome_email(user_email):
    subject = "Welcome to DRF Master!"
    message = "Thank you for registering at DRF Master. We're excited to have you on board!"
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    return send_mail(subject, message, email_from, recipient_list)
