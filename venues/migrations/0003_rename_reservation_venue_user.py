# Generated by Django 4.2.1 on 2023-06-11 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0002_rename_created_venue_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='reservation',
            new_name='user',
        ),
    ]