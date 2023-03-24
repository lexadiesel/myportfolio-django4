from django.shortcuts import render, get_object_or_404
from .models import Prospect

# Create your views here.

def home(request):
    prospects = Prospect.objects.all()
    return render(request,'portfolio/home.html', {'prospects':prospects})