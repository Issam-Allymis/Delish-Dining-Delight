# Generated by Django 3.2.22 on 2024-08-18 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_date_submitted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date_submitted',
        ),
    ]
