from django.db import models
from profiles.models import Profiles

# Create your models here.
class Report(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='reports',blank=True)
    remark = models.TextField()
    author = models.ForeignKey(Profiles,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"str({self.name})"