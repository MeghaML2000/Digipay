from django.shortcuts import render,redirect
from bankaccounts.models import Account,KYC
from django.db.models import Q
# q converts bigger or complex query to smaller or simple ones
from django.contrib import messages
from transations.models import transations


def search_user_by_account_number(request):
    account = Account.objects.all()

    query = request.POST.get("account_number")
    if query:
        account = account.filter(
            Q(account_number = query),
        ).distinct()

    context = {
        'account' :account,
        'query' : query

    }
    print(account)

    return render(request,"transations/search-user-by-account-number.html",context)

def amount_transfer(request,account_number):
    try :
        account = Account.objects.get(account_number=account_number)
    except:
        return messages("account does not exist")
    
    context={
        'account':account
    }

    return render(request,"transations/amount_transfer.html",context)

def amount_transfer_process(request,account_number):
    account = Account.objects.get(account_number=account_number)

    sender = request.user
    receiver = account.user

    sender_account = request.user.account
    receiver_account = account

    if request.method == "POST":
        amount = request.POST.get("amount-send")
        description = request.POST.get("description")

        print(amount)
        print(description)

        if sender_account.account_balance > 0  and amount:
            # amount is availabale balance and sender_account.amount is the user entered amount
            new_transation = transations.objects.create(
                transaction_id = transaction_id,
                user = request.user,
                description = description,
                amount = amount,
                sender_account = sender_account,
                sender = sender,
                receiver = receiver,
                receiver_account = receiver_account,
                status = "pending",
                transaction_type = "none"
            )
            new_transation.save()

            transaction_id = new_transation.transaction_id

            print(transaction_id)

            # creates saves the object details of transtion

    return render(request,"transations/amount_transfer_process.html")

def transfer_confirmation(request,account_number,transaction_id):

    try:
        account = Account.objects.get(account_number=account_number)
        transaction= transations.objects.get(transaction_id=transaction_id)
    except Account.DoesNotExist:
        messages.warning(request, "Account doesn't exist")
        return redirect('accounts:dashboard')
    except transations.DoesNotExist:
        messages.warning(request, "Transaction doesn't exist")
        return redirect('accounts:dashboard')
    
    context ={
        'account':account,
        'transaction':transaction,
        }
    
    return render(request,"transations/transfer_confirmation.html",context)

def transfer_success(request):

    try:
        pin_number = request.POST.get('pin_number')
    except:
        messages.warning(request, "Account doesn't exist")
    context = {
        'pin_number':pin_number
    }
    return render(request,"transations/transfer_success.html",context)