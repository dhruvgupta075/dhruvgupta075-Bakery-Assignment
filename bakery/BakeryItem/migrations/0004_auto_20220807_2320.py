# Generated by Django 3.1.1 on 2022-08-07 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BakeryItem', '0003_auto_20220805_0255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='cost_price',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='selling_price',
        ),
    ]