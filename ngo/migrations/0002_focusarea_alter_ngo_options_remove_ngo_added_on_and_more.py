# Generated by Django 4.1.7 on 2023-02-19 13:38

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FocusArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='ngo',
            options={},
        ),
        migrations.RemoveField(
            model_name='ngo',
            name='added_on',
        ),
        migrations.AddField(
            model_name='ngo',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ngo',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ngo',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ngo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='ngo',
            name='logo',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='ngo',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='ngo',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ngo',
            name='website_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='ngo',
            name='areas_of_focus',
            field=models.ManyToManyField(blank=True, to='ngo.focusarea'),
        ),
    ]
