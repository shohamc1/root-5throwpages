from django.db import models

# Create your models here.

class pagecontent (models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    name = models.TextField(default="noname")
    shortdesc = models.TextField(default="shortdesc")
    desc1 = models.TextField(default="desc1")
    desc2 = models.TextField(default="desc2")
    photo = models.ImageField(upload_to='images/', default='')