# Generated by Django 4.2.1 on 2023-09-20 06:16

from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('transations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transations',
            name='transaction_id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet=None, length=15, max_length=15, prefix='TRN', unique=True),
        ),
        migrations.AlterField(
            model_name='transations',
            name='updated_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]