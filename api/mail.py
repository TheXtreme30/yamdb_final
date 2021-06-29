import random
import string

from django.core.mail import send_mail


def generate_confirm_code():
    return ''.join(random.choices(string.digits + string.ascii_uppercase, k=6))


def send_mail_func(email, confirmation_code):
    send_mail(
        subject='Код подтверждения Yamdb',
        message=f'Код подтверждения {confirmation_code}',
        recipient_list=[email],
        fail_silently=False
    )
