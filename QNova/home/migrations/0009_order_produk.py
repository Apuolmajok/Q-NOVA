# Generated by Django 5.0.3 on 2024-04-22 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='produk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.produk'),
        ),
    ]