from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile

User =  get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender, instace, created, **kwargs):
    if created:
        Profile.objects.create(custome_user=instance)
        
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()