# Generated by Django 3.2.1 on 2025-07-21 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20250429_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user_type',
        ),
    ]
