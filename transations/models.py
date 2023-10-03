from django.db import models
from shortuuid.django_fields import ShortUUIDField
import uuid
from django.contrib.auth.models import User
from bankaccounts.models import Account
# Create your models here.

TRANSATION_STATUS = (
    ["FAILED","failed"],
    ["COMPLETED","completed"],
    ["PENDING","pending"],
    ["PROCESSING","processing"],
    ["REQUEST_SENT","request_sent"],
    ["REQUEST_PROCESSING","rquest_processing"],
)

TRANSATION_TYPE = (
    ["TRASFER","trasfer"],
    ["WITHDRAW","withdraw"],
    ["REFUND","refund"],
    ["RECEIVED","received"],
    ["REQUEST","request"],
    ["NONE","none"],
)
class transations(models.Model):
    transaction_id = ShortUUIDField(unique=True,length=15,max_length=25,prefix="TRN")

    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user",null=True)
    amount = models.DecimalField(max_digits=12,decimal_places=2,default=0.00)
    description = models.CharField(max_length=100)

    receiver = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,related_name="receiver")
    sender = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,related_name="sender")

    receiver_account = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True,related_name="receiver_amount")
    sender_account = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True,related_name="sender_amount")

    status =  models.CharField(max_length=100,choices=TRANSATION_STATUS,default="pending")
    transation_type =  models.CharField(max_length=100, choices=TRANSATION_TYPE,default="none")

    date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=False,null=True,blank=True)


    def __str__(self) :
        return f"{self.user}"