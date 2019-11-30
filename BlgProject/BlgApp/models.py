from django.db import models

# Create your models here.
class Upload(models.Model):
    name= models.CharField(max_length=255)
    pic= models.FileField(upload_to="images/")
    upload_date=models.DateTimeField(auto_now_add = True)
    author=models.CharField(max_length=255)
    description= models.TextField(default=' ')
