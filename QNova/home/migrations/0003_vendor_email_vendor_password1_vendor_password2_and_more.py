# Generated by Django 5.0.3 on 2024-04-17 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_customer_email_alter_customer_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='vendor',
            name='password1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='password2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='username',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
