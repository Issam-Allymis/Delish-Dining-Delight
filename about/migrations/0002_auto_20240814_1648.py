# Generated by Django 3.2.22 on 2024-08-14 15:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'About', 'verbose_name_plural': 'About'},
        ),
        migrations.RemoveField(
            model_name='about',
            name='content',
        ),
        migrations.AddField(
            model_name='about',
            name='history',
            field=models.TextField(blank=True, help_text='Brief history of the company', null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, help_text='Optional image for the About page', null=True, upload_to='about_images/'),
        ),
        migrations.AddField(
            model_name='about',
            name='milestones',
            field=models.TextField(blank=True, help_text="Key milestones in the company's history", null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='mission_statement',
            field=models.TextField(default='Our mission is to deliver quality service.', help_text='Mission statement of the company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date the About page was published'),
        ),
        migrations.AddField(
            model_name='about',
            name='values',
            field=models.TextField(blank=True, help_text='Core values of the company', null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(help_text='Title of the About page', max_length=200),
        ),
    ]
