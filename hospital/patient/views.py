from django.shortcuts import render
from .models import PatientInfo
# Create your views here.
def show(r):
    Pdetails = PatientInfo.objects.all() #ORM
    mydict = {'Pdetails':Pdetails}

    return render(r,'patient.html',context=mydict)

# Create your views here.
