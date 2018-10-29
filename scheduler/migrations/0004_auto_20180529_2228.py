# Generated by Django 2.0.4 on 2018-05-29 22:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_auto_20180529_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='referee',
            name='grade',
            field=models.IntegerField(default=8, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='referee',
            name='is_certified',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='referee',
            name='years_experience',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]
