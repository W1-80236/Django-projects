from django.db import models

# Create your models here.
class PatientInfo(models.Model):
    pname = models.CharField(max_length=20)
    #paddress = models.CharField(max_length=25)
    admitdate= models.DateField(auto_created=True)
    disdate= models.DateField(auto_created=True)
    mailid= models.EmailField()
