# Generated by Django 4.2 on 2023-05-05 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nw_orders_app', '0009_order_spline_alter_wood_options_orderitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('order_date',)},
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now=True),
        ),
    ]
