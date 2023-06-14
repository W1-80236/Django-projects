from django.db import models

# Create your models here.
class Classicbooks(models.Model):
    bname = models.CharField(max_length=20)
    bqnty = models.IntegerField()
    bauthor = models.CharField(max_length=20)
    bprice = models.IntegerField()
    bpublication = models.CharField(max_length=25)
    bpublisheddate= models.DateField(auto_created=True)
