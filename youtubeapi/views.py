from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    c = Vidata.objects.values()
    context = {"data":c}
    return render(request, 'index.html', context)


