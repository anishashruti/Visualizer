from .models import Sale
#many to many changes
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

@receiver(m2m_changed,sender=Sale.positions.through)
def calculate(sender,instance,action,**kwargs):
    total=0
    if action=='post_remove' or action=='post_add':
        for item in instance.get_postions():
            total+=item.price

    instance.total=total
    instance.save()