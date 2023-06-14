from django.shortcuts import render
from .models import Classicbooks
# Create your views here.
def show(r):
    booklist = Classicbooks.objects.all() #ORM
    mydict = {'booklist':booklist}

    return render(r,'showbooks.html',context=mydict)