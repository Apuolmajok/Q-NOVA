# Generated by Django 5.0.3 on 2024-03-31 01:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_shippingaddress_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=16)),
                ('description', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('image1', models.ImageField(upload_to='uploads/products/')),
                ('is_sale', models.BooleanField(default=False)),
                ('sale_price', models.DecimalField(decimal_places=2, default=0, max_digits=16)),
                ('Category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
