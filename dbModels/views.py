from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Lga, Polling_unit
from .forms import PU_result_add_form

# Create your views here.

lga = Lga.objects.order_by('lga_name')
context = {
    'lgas':lga,
}

def home(request):

    return render(request,'index.html')

def pu(request):

    if request.method == 'POST':
        lga_req = request.POST['lga']
        ward_req = request.POST['ward']
        pu_req = request.POST['pu']

        print(f'lga:{lga_req}, ward:{ward_req}, pu:{pu_req}')


    return render(request, 'pu.html', context)

def lga(request):
    if request.method == 'POST':
        lga_req = request.POST['lga']

        # making queries to get all announced result of a particular lga
        res = Lga.objects.get(lga_id=lga_req)
        res1= res.announced_lga_results_set.all()
        result_dict = {p.party_abbreviation:p.party_score for p in res1}
        # print(result_dict)

        return render(request, 'lga.html', {'result_dict':result_dict,'lgas':Lga.objects.order_by('lga_name')})
        
    return render(request, 'lga.html',context)

def new_pu(request):

    if request.method == 'POST':
        f = PU_result_add_form(request.POST)
        f.save()
        return HttpResponseRedirect(reverse('dbModels:home'))
        # return HttpResponseRedirect('/thanks/')
    else:
        f = PU_result_add_form()
    return render(request, 'new_pu_result.html',{'form':f})