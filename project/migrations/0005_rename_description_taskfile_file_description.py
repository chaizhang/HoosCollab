# Generated by Django 5.1.1 on 2024-11-08 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_remove_taskfile_org_taskfile_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskfile',
            old_name='description',
            new_name='file_description',
        ),
    ]