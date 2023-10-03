from django.urls import path
from bankaccounts import views

app_name = 'bankaccounts'

urlpatterns = [
    
    path('',views.KYC_registeration),
]