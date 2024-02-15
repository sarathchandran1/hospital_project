from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Departments, Doctors
from .forms import BokkingForm
# Create your views here.


def index(request):
   
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == 'POST':
        form = BokkingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confarmation.html')
    form = BokkingForm()
    dict_form={
        'form': form
    }
    return render(request, 'booking.html', dict_form)

def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)

def contact(request):
    return render(request, 'contact.html')

def department(request):
   dict_dept={
      'dept': Departments.objects.all()
   }

   return render(request, 'department.html', dict_dept)

