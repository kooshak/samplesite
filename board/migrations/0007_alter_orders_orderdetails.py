# Generated by Django 4.1 on 2022-12-07 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_remove_orders_order_orders_orderdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='ORDERDETAILS',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='board.orderdetails'),
        ),
    ]
