from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
# Create your models here.

def home(request):
    destination = Destination()
    destination.image = "destination_1.jpg"
    destination.destination = "Mumbai"
    destination.description = "City that never sleep."
    destination.price = 76
    destination.offer = True
    return render(request, "index.html", {'destini': [destination, destination]})


def about(request):
    return render(request, "about.html")
