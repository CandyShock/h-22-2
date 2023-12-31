from django.conf import settings
from django.core.mail import send_mail


def send_new_pass(email, new_password):
    send_mail(
        subject='Password change',
        message=f'You password:{new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )