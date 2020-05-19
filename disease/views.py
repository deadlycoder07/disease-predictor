from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Diseases, symptoms
from .forms import Diseaseform, Symptomform


# Create your views here.
def home(request):
    return render(request, 'disease/base.html')

    
def thanks(request):
    return render(request, 'disease/thanks.html')

    
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
    
    data = str(getattr(symp, str(field), "null"))
    #print(field)
    #print(symp)
    
    if("," in data):
        data = data.split(",")
    else:
        data = data.strip(" ")

    #data is available for analysis
    symptoms.objects.all().delete()

    return render(request, 'disease/analysis.html')

