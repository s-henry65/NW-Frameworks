# Generated by Django 4.2 on 2023-05-31 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nw_orders_app', '0021_radius_alter_order_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Radius',
            new_name='Corner',
        ),
        migrations.AlterModelOptions(
            name='corner',
            options={'ordering': ('name',)},
        ),
    ]
