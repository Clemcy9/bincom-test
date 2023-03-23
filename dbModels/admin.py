from django.contrib import admin
from .models import Agent, Party, Polling_unit, Lga, State, Ward, Announced_pu_results,Announced_lga_results,Announced_ward_results,Announced_state_results


# Register your models here.

admin.site.register([Agent,Party,Polling_unit,Lga,State,Ward, Announced_lga_results,Announced_pu_results])
