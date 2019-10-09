from django.db import models

# Create your models here.

class pagecontent (models.Model):
    name = models.TextField(default="noname")
    shortdesc = models.TextField(default="shortdesc")
    desc1 = models.TextField(default="desc1")
    desc2 = models.TextField(default="desc2")