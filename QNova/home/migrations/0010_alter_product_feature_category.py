# Generated by Django 5.0.3 on 2024-03-31 01:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_image1_product_feature_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_feature',
            name='Category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.category'),
        ),
    ]
