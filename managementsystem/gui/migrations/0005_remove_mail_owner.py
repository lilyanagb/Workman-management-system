# Generated by Django 4.1.4 on 2023-02-17 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0004_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='owner',
        ),
    ]
