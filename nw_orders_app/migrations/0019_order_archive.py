# Generated by Django 4.2 on 2023-05-13 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nw_orders_app', '0018_order_order_delivered_order_order_paid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
