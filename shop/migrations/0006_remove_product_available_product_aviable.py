# Generated by Django 4.0.3 on 2022-05-07 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_aviable_product_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available',
        ),
        migrations.AddField(
            model_name='product',
            name='aviable',
            field=models.BooleanField(default=True),
        ),
    ]