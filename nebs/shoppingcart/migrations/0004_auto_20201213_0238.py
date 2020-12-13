# Generated by Django 3.1.3 on 2020-12-13 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0003_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='clients',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='order',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoppingcart.client'),
        ),
    ]
