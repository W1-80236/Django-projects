from django.shortcuts import render

# Create your views here.
def hmovies(r):
    return render(r,'hollywood/avanger.html')