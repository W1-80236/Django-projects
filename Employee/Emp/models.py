from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    E_id = models.IntegerField()
    E_name = models.CharField(max_length=20)
    E_city = models.CharField(max_length=20)
    E_dob = models.DateField(auto_created=True)
    E_mail = models.EmailField()
    class Meta:
        db_table='EmployeeDetails'