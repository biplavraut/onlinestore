# Generated by Django 3.2.3 on 2021-06-30 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210630_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
