# Generated by Django 5.0 on 2024-01-08 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_module_s1_profile_module_selection_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='module_Selection_1',
            new_name='module_Selection_1_ID_Number',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='module_Selection_2',
            new_name='module_Selection_2_ID_Number',
        ),
    ]
