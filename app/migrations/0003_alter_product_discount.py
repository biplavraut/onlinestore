# Generated by Django 3.2.4 on 2021-06-27 03:08

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.FloatField(default=app.models.calculate_discount),
        ),
    ]
