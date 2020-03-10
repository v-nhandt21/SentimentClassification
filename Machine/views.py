import re
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Machine.forms import DetectionForm, thachthucForm

####################################################################


#def home(request):
#    return HttpResponse("Hello, Django!")

def home(request):
    return render(
        request, 
        "Machine/home.html",
        {
            'date': datetime.now()
        }
    )

def about(request):
    return render(request, "Machine/about.html")

def paper(request):
    return render(request, "Machine/paper.html")

def demo(request):
    form= DetectionForm()
    result=""
    if request.method == "POST":
        form=DetectionForm(request.POST)
        result="Nhan"
        result=form.result
    return render(request, 
                    "Machine/demo.html", 
                    {
                        'form': form,
                        'result': result
                    }
                )

def thachthuc(request):
    form= thachthucForm()
    result=""
    if request.method == "POST":
        form=thachthucForm(request.POST)
        result="Nhan"
        result=form.result
    return render(request, 
                    "Machine/thachthuc.html", 
                    {
                        'form': form,
                        'result': result
                    }
                )




