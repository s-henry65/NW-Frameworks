# Generated by Django 4.2 on 2023-04-29 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nw_orders_app', '0007_rename_price_wood_price_modifier_alter_wood_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finish',
            old_name='price',
            new_name='price_modifier',
        ),
    ]
