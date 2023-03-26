from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Lga, Polling_unit
from .forms import PU_result_form

# Create your views here.

lga = Lga.objects.order_by('lga_name')
context = {
    'lgas':lga,
}

def home(request):

    return render(request,'index.html')

def pu(request):

    return render(request, 'pu.html', context)

def lga(request):
    return render(request, 'lga.html',context)

def new_pu(request):

    if request.method == 'POST':
        f = PU_result_form(request.POST)
        f.save()
        # return HttpResponseRedirect(reverse('dbModels:home'))
        return HttpResponseRedirect('/thanks/')
    else:
        f = PU_result_form()
    return render(request, 'new_pu_result.html',{'form':f})