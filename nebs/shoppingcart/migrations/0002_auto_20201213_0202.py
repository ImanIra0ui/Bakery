# Generated by Django 3.1.3 on 2020-12-13 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Number',
            field=models.IntegerField(),
        ),
    ]
