from django.shortcuts import render

# Create your views here.
def bmovies(r):
    return render(r,'bollywood/ddlj.html')