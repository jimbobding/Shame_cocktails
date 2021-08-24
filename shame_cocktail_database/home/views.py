from django.shortcuts import render
from .models import Drinks


def home(request):

    context = {
        'drinks': Drinks.objects.all()
    }
    return render(request, "home/index.html", context)

# Create your views here.
