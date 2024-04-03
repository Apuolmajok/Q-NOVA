# Generated by Django 5.0.1 on 2024-04-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_rename_description_testimonials_description1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Blogcategories',
            },
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='Category',
            new_name='blogcategory',
        ),
    ]