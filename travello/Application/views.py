from django.shortcuts import render
from django.http import HttpResponse
from models import Destination

# Create your views here.
# Create your models here.
class Destination:
    image: str
    destination: str
    description: str
    price: int

def home(request):
    destination = Destination()
    destination.image = "destination_1.jpg"
    destination.destination = "Mumbai"
    destination.description = "City that never sleep."
    destination.price = 765
    return render(request, "index.html", {'destini': [destination, destination]})


def about(request):
    return render(request, "about.html")
