# Generated by Django 3.2.3 on 2021-06-24 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210624_0455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='latestblog',
            old_name='latest_blog',
            new_name='blog_name',
        ),
        migrations.AddField(
            model_name='latestblog',
            name='img',
            field=models.ImageField(default=111, upload_to='images'),
            preserve_default=False,
        ),
    ]
