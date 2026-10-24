from django.contrib import messages
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver


@receiver(user_logged_in)
def welcome_user(sender, request, user, **kwargs):
    messages.success(
        request,
        "Welcome!",
        extra_tags="welcome-popup",
    )