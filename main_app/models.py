from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

# Create your models here.

class Total(models.Model):
  total = models.IntegerField(default=0)

class Widget(models.Model):
  description = models.CharField(max_length=50)
  quantity = models.IntegerField()
  # total = models.ForeignKey(Total, null=True, on_delete=models.CASCADE)

# @receiver(post_save, sender=Widget)
# def update_total(sender, instance, **kwargs):
#   line_quantity = instance.quantity
#   instance.total += line_quantity

# @receiver(pre_delete, sender=Widget)
# def delete_total(sender, instance, **kwargs):
#   line_quantity = instance.quantity
#   instance.total -= line_quantity