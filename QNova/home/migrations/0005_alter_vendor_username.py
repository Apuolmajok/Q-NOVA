# Generated by Django 5.0.3 on 2024-04-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_password1_vendor_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='username',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
