# Generated by Django 5.1.3 on 2024-11-12 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plantations', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(choices=[('kg', 'كيلو'), ('box', 'سلة'), ('bundle', 'ربطة'), ('cup', 'قدح'), ('bag', 'كيس')], max_length=150)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantations.plants')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(choices=[('kg', 'كيلو'), ('box', 'سلة'), ('bundle', 'ربطة'), ('cup', 'قدح'), ('bag', 'كيس')], max_length=100)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField(default=False)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantations.plants')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_image', models.ImageField(null=True, upload_to='photo/%y/%m/%d')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unite', models.CharField(choices=[('kg', 'كيلو'), ('box', 'سلة'), ('bandle', 'ربطة'), ('cup', 'قدح'), ('bag', 'كيس')], max_length=100)),
                ('unite_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pr_date', models.DateField(auto_now_add=True)),
                ('ex_date', models.DateField()),
                ('product_state', models.BooleanField(default=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantations.categories')),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantations.crops')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valuation', models.IntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('revewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='given_reviews', to='users.user')),
                ('reviewed_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_reviews', to='users.user')),
            ],
        ),
    ]