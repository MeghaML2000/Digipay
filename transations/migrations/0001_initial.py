# Generated by Django 4.2.1 on 2023-09-20 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bankaccounts', '0002_rename_imgae_kyc_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='transations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=22, max_length=25, prefix='TRN', unique=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('description', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[['FAILED', 'failed'], ['COMPLETED', 'completed'], ['PENDING', 'pending'], ['PROCESSING', 'processing'], ['REQUEST_SENT', 'request_sent'], ['REQUEST_PROCESSING', 'rquest_processing']], default='pending', max_length=100)),
                ('transation_type', models.CharField(choices=[['TRASFER', 'trasfer'], ['WITHDRAW', 'withdraw'], ['REFUND', 'refund'], ['RECEIVED', 'received'], ['REQUEST', 'request'], ['NONE', 'none']], default='none', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('receiver_amount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receiver_amount', to='bankaccounts.account')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender', to=settings.AUTH_USER_MODEL)),
                ('sender_amount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender_amount', to='bankaccounts.account')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
