# Generated by Django 5.0.3 on 2024-03-31 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_product_feature_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_feature',
            name='Category',
        ),
    ]
