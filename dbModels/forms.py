from django.forms import ModelForm
from .models import Announced_pu_results

class PU_result_form(ModelForm):

    class Meta:
        model = Announced_pu_results

        fields = '__all__'
        exclude = ['unique_id']