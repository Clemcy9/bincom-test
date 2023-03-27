from django.forms import ModelForm
from .models import Announced_pu_results, Announced_lga_results, Polling_unit

class PU_result_add_form(ModelForm):

    class Meta:
        model = Announced_pu_results

        fields = '__all__'
        exclude = ['unique_id']

# class lGA_result_form(ModelForm):

#     class Meta:
#         model = Announced_lga_results

#         fields = '__all__'
#         exclude = ['unique_id']

class PU_result_check_form(ModelForm):

    class Meta:
        model = Polling_unit

        fields = ['ward_id','lga_id']