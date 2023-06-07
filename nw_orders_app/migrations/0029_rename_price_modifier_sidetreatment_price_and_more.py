# Generated by Django 4.2 on 2023-06-07 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nw_orders_app', '0028_alter_sidetreatment_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sidetreatment',
            old_name='price_modifier',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='toptreatment',
            old_name='price_modifier',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='gold',
        ),
        migrations.RemoveField(
            model_name='sidetreatment',
            name='gold',
        ),
        migrations.RemoveField(
            model_name='toptreatment',
            name='gold',
        ),
        migrations.DeleteModel(
            name='Gold',
        ),
    ]
