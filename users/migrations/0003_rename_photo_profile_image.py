# Generated by Django 5.0 on 2024-01-07 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_image_profile_photo_profile_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='photo',
            new_name='image',
        ),
    ]