# Generated by Django 4.1.3 on 2023-04-15 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('con', '0002_con_created_at_con_is_active_con_updated_at'),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('request_id', models.CharField(max_length=255, verbose_name='Order number')),
                ('client_iin', models.CharField(max_length=255, verbose_name='Client IIN')),
                ('taker_iin', models.CharField(max_length=255, verbose_name='Taker IIN')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In progress'), ('done', 'Done')], max_length=255, verbose_name='Status')),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.address', verbose_name='Address')),
                ('con_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='con.con', verbose_name='Con')),
                ('courier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Courier')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('old_status', models.CharField(blank=True, max_length=255, null=True, verbose_name='Old status')),
                ('new_status', models.CharField(blank=True, max_length=255, null=True, verbose_name='New status')),
                ('new_courier_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='new_courier', to=settings.AUTH_USER_MODEL, verbose_name='New courier')),
                ('old_courier_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='old_courier', to=settings.AUTH_USER_MODEL, verbose_name='Old courier')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'OrderHistory',
                'verbose_name_plural': 'OrderHistories',
            },
        ),
    ]
