# Generated by Django 3.1.3 on 2020-12-13 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0004_auto_20201213_0238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='owner',
        ),
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shoppingcart.client'),
        ),
    ]
