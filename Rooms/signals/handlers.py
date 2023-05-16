from django.dispatch import receiver
from Rooms.models import *
from django.db.models.signals import post_delete, pre_save
from django.utils.text import slugify


@receiver(pre_save, sender=Rooms)
def pre_save_movies_post_receiever(sender, instance, *args, **kwargs):
    instance.slug = slugify(str(instance.room_number))
		
@receiver(post_delete, sender=Rooms)
def submission_delete(sender, instance, **kwargs):
    instance.room_image.delete(False) 