# Generated by Django 3.1.3 on 2021-01-06 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0011_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]