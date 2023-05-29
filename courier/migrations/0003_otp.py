# Generated by Django 4.1.3 on 2023-04-15 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0002_couriercouriercenter'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('phone', models.CharField(max_length=255, verbose_name='Phone')),
                ('otp', models.CharField(max_length=255, verbose_name='OTP')),
                ('is_verified_by_con', models.BooleanField(default=False, verbose_name='Is verified by con')),
            ],
            options={
                'verbose_name': 'OTP',
                'verbose_name_plural': 'OTPs',
            },
        ),
    ]