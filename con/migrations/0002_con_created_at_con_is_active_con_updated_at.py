# Generated by Django 4.1.3 on 2023-04-15 10:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('con', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='con',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='con',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='con',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
