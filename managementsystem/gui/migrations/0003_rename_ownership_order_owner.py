# Generated by Django 4.1.4 on 2023-02-16 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0002_remove_order_username_order_ownership'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ownership',
            new_name='owner',
        ),
    ]
