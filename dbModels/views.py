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
        # announced result
        res1= res.announced_lga_results_set.all()
        announced_result_dict = {p.party_abbreviation:p.party_score for p in res1}
        # print(result_dict)
        
        # calculated result
        calc_pu = res.polling_unit_set.all()[0].announced_pu_results_set.all()
        print(f'calc_pu:{calc_pu}')
        # one = calc_pu[0]
        # print(f'one:{one}')
        # one_res = one.announced_pu_results_set.all()
        # print(f'one_res{one_res}')
        # calc_annouced_pu_result = [x.announced_pu_results_set.all() for x in calc_pu ]
        # print(f'calc_announced_pu_result {calc_annouced_pu_result}')
        # calc_pu_res = calc_pu_res.party_score
        # party_calc_result =[]
        # print(f'many result: {calc_pu}')
        # print(f'one result: {type(res)}')
        # print(f'calc polling unit: {calc_announced_polling_result}')
        # print(f'calc polling list: {calc_announced_result_list}')


        return render(request, 'lga.html', {'result_dict':announced_result_dict,'lgas':Lga.objects.order_by('lga_name')})
        
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

def tshirt(request):
    return render(request,'shirt.html')