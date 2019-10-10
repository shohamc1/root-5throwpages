from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import pagecontent

# Create your views here.

def page (request):
    if request.method == 'POST':
        request.session['inputid'] = int(request.POST.get('inputid'))
        return HttpResponseRedirect(reverse('pages:page'))
    else:
        data = pagecontent.objects.all()
        inputid = request.session.get('inputid')
        print (inputid)
        return render (request, 'main.html', {'data': data, 'testid': inputid})

def upload (request):
    if request.method == 'POST':
        #add new data
        newitem = pagecontent(id = request.POST.get('id'), name = request.POST.get('name'), shortdesc = request.POST.get('shortdesc'), desc1 = request.POST.get('desc1'), desc2 = request.POST.get('desc2'), photo = request.FILES['photo'])
        newitem.save()
        return HttpResponseRedirect (reverse('pages:upload'))
    
    else:
        #show the form
        return render (request, 'form.html')