# Generated by Django 5.0.3 on 2024-04-17 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_vendor_email_vendor_password1_vendor_password2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='password1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='password2',
        ),
    ]