# Generated by Django 4.0.3 on 2022-05-07 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_product_available_product_aviable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='aviable',
            new_name='available',
        ),
    ]
