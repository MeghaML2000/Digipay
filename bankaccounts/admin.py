from django.contrib import admin
from bankaccounts.models import Account,KYC

# Register your models here.
class AccountAdmin(admin.ModelAdmin) :
    list_display = ['user','account_number','account_balance','account_status','kyc_submitted','kyc_confirmed']
    list_editable = ['account_balance','account_status','kyc_submitted','kyc_confirmed']

admin.site.register(Account,AccountAdmin)

class AccountAdmin(admin.ModelAdmin) :
    list_display = ['user','full_name','gender','identity_type','phone']
    # list_editable = []

admin.site.register(KYC,AccountAdmin)