from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .models import Diseases, symptoms,alert
from .forms import Diseaseform, Symptomform


def home(request):
    context={}
    alerts=alert.objects.all().order_by('affected_by')
    context['alerts']=alerts
    return render(request, 'disease/home.html',context)

def contact(request):
    return render(request, 'disease/contact.html')

def aboutus(request):
    return render(request, "disease/aboutus.html")

def privacy(request):
    return render(request, 'disease/privacy.html')
    
def thanks(request):
    return render(request, 'disease/thanks.html')

def Hhome(request):
    return render(request, 'disease/HospitalDash.html')
    
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

