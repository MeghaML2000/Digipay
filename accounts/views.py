from django.shortcuts import render
from accounts.forms import user_form
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def register(request):
    registered = False
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, your account was created successfully..")

            registered = True
    else:
        form = user_form()
    return render(request,"account/register.html",{'form':form,'registered' : registered})
        

def signin(request) :

    if request.method == 'POST' :

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user :
            if user.is_active :
                login(request,user)
                print(username)
                print(password)
                return redirect('accounts:dashboard')
            
        else :
            return HttpResponse("PLEASE CHECK YOUR CREDENTIALS......!!!!!")
        
    return render(request,"account/signin.html")

def dashboard(request) :
    return render(request,"account/dashboard.html")

def account(request):
    msg = {
        'text':'this is account page'
    }
    return render(request,"account/account.html",msg)