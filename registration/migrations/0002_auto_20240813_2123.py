# Generated by Django 3.2.22 on 2024-08-13 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
