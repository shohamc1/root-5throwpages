from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import pagecontent
from .forms import FifthForm

# Create your views here.

def page (request):
    data = pagecontent.objects.all()
    return render (request, 'main.html', {'data': data})

def upload (request):
    if request.method == 'POST':
        #add new data
        #newitem = pagecontent(id = request.POST.get('id'), name = request.POST.get('name'), shortdesc = request.POST.get('shortdesc'), desc1 = request.POST.get('desc1'), desc2 = request.POST.get('desc2'), photo = request.POST.get('photo'))
        #newitem.save()
        form = FifthForm(request.POST, request.FILES)
        if form.is_valid():
            data.save()
            return HttpResponseRedirect (reverse('pages:upload'))
        else:
            return render(request, 'form.html', {form: 'form'})
    
    else:
        #show the form
        return render (request, 'form.html')