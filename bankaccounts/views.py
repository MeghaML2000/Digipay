from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from bankaccounts.models import Account,KYC
from bankaccounts.forms import KYC_form
from django.contrib.auth.decorators import login_required

# Create your views here.

def KYC_registeration(request):
    user = request.user 
    account = Account.objects.get(user=user)

    try:
        kyc = KYC.objects.get(user=user)
    except:
        kyc = None

    if request.method == "POST":
        form = KYC_form(request.POST,request.FILES,instance=kyc)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account 
            new_form.save()
            messages.success(request, "KYC Form submitted successfully, In review now.") 
            return redirect("dashboard")
    else:
        form = KYC_form(instance=kyc)
    context = {
        "account": account,
        "form": form,
        "kyc": kyc,
    }
    return render(request,"account/kyc-form.html",context)

@login_required
def account(request):
    kyc = KYC.objects.get(user=request.user)
    account = Account.objects.get(user=request.user)
    context = {
        'kyc' : kyc,
        'account': account
        }
    return render(request,"account/account.html",context)
