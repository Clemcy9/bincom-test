from django.urls import path
from .views import home,pu,lga,new_pu

app_name = 'dbModels'

urlpatterns = [
    path('',home,name='home'),
    path('pu-res/',pu,name='pu_result'),
    path('lga-res/',lga,name='lga_result'),
    path('new-pu',new_pu,name='new_pu'),
]