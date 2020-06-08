from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .models import Diseases, symptoms, alert, question, answer
from .forms import Diseaseform, Symptomform, QuestionForm


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
    
    data_symp = str(getattr(symp, str(field), "null"))
    #print(field)
    #print(symp)
    
    if("," in data_symp):
        data_symp = data_symp.split(",")
    else:
        data_symp = data_symp.strip(" ")

    #data_symp is available for analysis
    symptoms.objects.all().delete()       

    return render(request, 'disease/analysis.html')

def qanalysis(request):
    ans = answer.objects.all()
    field = answer._meta.fields

    data_ans = str(getattr(ans, str(field), 'null'))

    if("," in data_ans):
        data_ans = data_ans.split(",")
    else:
        data_ans = data_ans.strip(" ")

    answer.objects.all().delete()

    return render(request, 'disease/analysis.html')


def userquestion(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'disease/analysis.html')
    else:
        form = QuestionForm()
    return render(request, 'disease/userquestion.html', {'form' : form})