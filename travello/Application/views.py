from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
# Create your models here.

def home(request):
    print(Destination.objects.last())
    dest = Destination.objects.all()
    return render(request, "index.html", {'destini': dest})


def about(request):
    return render(request, "about.html")
