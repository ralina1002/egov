# Generated by Django 4.1.3 on 2023-04-15 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourierCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('address_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.address', verbose_name='Address')),
            ],
            options={
                'verbose_name': 'CourierCenter',
                'verbose_name_plural': 'CourierCenters',
            },
        ),
    ]
