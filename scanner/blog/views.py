from django.shortcuts import render
from .models import Devices
#from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    context = {
        "Devices": Devices.objects.all()
    }
    return render(request, 'blog/index.html', context)
