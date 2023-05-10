# Generated by Django 4.2 on 2023-05-07 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nw_orders_app', '0010_alter_order_options_alter_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='frame_price',
            field=models.DecimalField(decimal_places=2, default=99, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='price_ui',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='ui',
            field=models.DecimalField(decimal_places=2, default=60, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='notes',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
