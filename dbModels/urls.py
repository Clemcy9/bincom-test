from django.urls import path
from .views import home

urlpatterns = [
    path('',home,name='home'),
    # path('/pu-res/',,name='polling_unit_result'),
    # path('lga-res/',,name='lga_result'),
    # path('new-pu',,name='create_pu'),
]