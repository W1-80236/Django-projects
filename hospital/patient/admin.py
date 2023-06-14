from django.contrib import admin
from .models import PatientInfo

# Register your models here.
class Pdetails(admin.ModelAdmin):
    list_display= [
        'pname',
        #'paddress ',
        'admitdate',
        'disdate',
        'mailid',
    ]
admin.site.register(PatientInfo, Pdetails)