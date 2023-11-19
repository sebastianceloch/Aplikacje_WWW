from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    from rest_framework.authtoken.models import Token
    if created:
        Token.objects.create(user=instance)
class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
