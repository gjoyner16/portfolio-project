from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
