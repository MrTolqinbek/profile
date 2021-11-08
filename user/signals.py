from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete


def profileCreated(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username
        )


def deleteProfile(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(profileCreated, sender=User)
post_delete.connect(deleteProfile, sender=Profile)
