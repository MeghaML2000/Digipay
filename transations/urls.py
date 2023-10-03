from django.urls import path
from transations import transfer

app_name = 'transations'

urlpatterns = [
    
    path('',transfer.search_user_by_account_number,name='search'),
    path('amount_transfer/<account_number>/',transfer.amount_transfer,name='amount_transfer'),
    path('amount_transfer_process/<account_number>/',transfer.amount_transfer_process,name='amount_transfer_process'),
    path('transfer_confirmation/<account_number>/<transaction_id>/',transfer.transfer_confirmation,name='transfer_confirmation'),
    path('transfer_success/',transfer.transfer_success,name='transfer_success'),

]