# Generated by Django 4.2 on 2023-06-07 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nw_orders_app', '0027_alter_orderitem_gold_cost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sidetreatment',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='toptreatment',
            options={'ordering': ('name',)},
        ),
    ]
