from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Diseases
from .forms import Diseaseform


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

