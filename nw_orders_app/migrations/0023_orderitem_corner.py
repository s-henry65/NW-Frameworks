# Generated by Django 4.2 on 2023-05-31 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nw_orders_app', '0022_rename_radius_corner_alter_corner_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='corner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nw_orders_app.corner'),
        ),
    ]
