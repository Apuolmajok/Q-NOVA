# Generated by Django 5.0.3 on 2024-03-31 00:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_date_order_date_ordered_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='date_added',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]