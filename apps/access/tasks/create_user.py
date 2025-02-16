from celery import shared_task

from apps.access.models import User


@shared_task
def create_user_dynamically():
    """Create users."""

    email = "testuser"
    for iteration in range(1, 15):
        User.objects.create(email=f"{email}{iteration}@mailinator.com")

    return True
