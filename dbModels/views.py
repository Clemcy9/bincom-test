from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,'index.html')

def pu(request):
    return render(request, 'pu.html')

def lga(request):
    return render(request, 'lga.html')

def new_pu(request):
    return render(request, 'new_pu.html')