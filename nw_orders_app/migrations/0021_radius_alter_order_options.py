# Generated by Django 4.2 on 2023-05-30 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nw_orders_app', '0020_alter_order_order_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Radius',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('id',)},
        ),
    ]
