# Generated by Django 5.1.3 on 2024-11-13 22:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='ex_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='image',
            field=models.ImageField(null=True, upload_to='photo/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='inventory_state',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='pr_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='inventory',
            name='unite_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
