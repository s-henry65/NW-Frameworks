# Generated by Django 4.2 on 2023-05-10 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nw_orders_app', '0015_alter_order_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='notes',
        ),
        migrations.AddField(
            model_name='order',
            name='notes',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
