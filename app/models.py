from django.db import models

# Create your models here.
class Stu(models.Model):
	name=models.CharField(max_length=200)
	section=models.CharField(max_length=200)
	img=models.ImageField(blank=True, upload_to="images/")

