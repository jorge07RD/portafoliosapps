from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class noteblock(models.Model):
    Subject = models.CharField(max_length=50)
    note = models.CharField(max_length=1500,blank=True,null=True)
    TYPE_SELECT = [
        ('dark', 'dark'),
        ('success', 'success'),
        ('info', 'info'),
        ('warning', 'warning'),
        ('danger', 'danger'),
    ]
    color = models.CharField(max_length=11,choices=TYPE_SELECT)

