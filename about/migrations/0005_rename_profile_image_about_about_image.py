# Generated by Django 4.2.9 on 2024-02-08 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_about_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='profile_image',
            new_name='about_image',
        ),
    ]
