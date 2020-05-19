from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Diseases, symptoms
from .forms import Diseaseform, Symptomform


# Create your views here.

def thanks(request):
    return render(request, 'disease, thanks.html')

    
def diseaseview(request):
    if request.method == "POST":
        form = Diseaseform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'disease/thanks.html')
    else:
        form = Diseaseform()
    
    return render(request, 'disease/form.html', {'form' : form})

def usercheckview(request):
    if request.method == "POST":
        form = Symptomform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'disease/analysis.html')
    else:
        form = Symptomform()

          

    return render(request, 'disease/usercheck.html', {'form' : form})

def analysis(request):
    symp = symptoms.objects.all()
    field = symptoms._meta.fields
    print(field)
    print(symp)
    return render(request, 'disease/analysis.html')

