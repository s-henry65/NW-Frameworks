# Generated by Django 4.2 on 2023-06-04 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nw_orders_app', '0025_orderitem_gold_cost_orderitem_gold_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='gold_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
