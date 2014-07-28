from django.db import models

# Create your models here.
class DemoClass(models.Model):
  title = models.CharField(max_length=500)
  description=models.TextField(max_length=2000)