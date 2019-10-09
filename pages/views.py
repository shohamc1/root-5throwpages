from django.shortcuts import render
from .models import pagecontent

# Create your views here.

def page (request):
    data = pagecontent.objects.all()
    return render (request, 'main.html', {'data': data})