# Generated by Django 4.1.3 on 2023-04-16 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='is_verified_by_con',
            field=models.BooleanField(default=False, verbose_name='Is verified by con'),
        ),
    ]