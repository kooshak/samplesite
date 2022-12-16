# Generated by Django 4.1 on 2022-12-07 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_alter_orders_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='ORDER',
        ),
        migrations.AddField(
            model_name='orders',
            name='ORDERDETAILS',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='board.orderdetails'),
        ),
    ]