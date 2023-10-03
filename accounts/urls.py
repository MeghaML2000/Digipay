from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    
    path('',views.signin,name='signin'),
    path('register/',views.register,name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('account/',views.account,name='account'),

]