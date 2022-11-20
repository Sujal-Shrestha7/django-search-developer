from .models import Profiles
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print('update_profile')
    if created:
        user = instance
        profile = Profiles.objects.create(
            user=user,
            username=user.username,
            email=user.email
        )
        subject = 'Welcome to Facebook'
        message = 'We are glad to have you here. Click here to submit your cv. https://meta.facebook.register-form'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False

        )


@receiver(post_save, sender=Profiles)
def update_profile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.first_name = profile.name
        user.username = profile.username.upper()
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profiles)
def delete_profile(sender, instance, **kwargs):
    print('profile deleting....')
    user = instance.user
    user.delete()

# non preferable way of connecting receiver instead use decorators
# post_save.connect(update_profile, sender=Profiles)
# post_delete.connect(delete_profile, sender=Profiles)
