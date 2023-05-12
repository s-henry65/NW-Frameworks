# Generated by Django 4.2 on 2023-05-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nw_orders_app', '0016_remove_orderitem_notes_order_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='frame_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
