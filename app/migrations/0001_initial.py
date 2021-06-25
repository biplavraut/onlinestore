# Generated by Django 3.2.3 on 2021-06-25 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('brand_tagline', models.CharField(max_length=200)),
                ('logo', models.ImageField(default='noimg.png', null=True, upload_to='brand_logo')),
                ('display', models.BooleanField(default=True)),
                ('brand_description', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LatestBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=100)),
                ('blog_description', models.TextField()),
                ('release_date', models.DateTimeField(verbose_name='date released')),
                ('img', models.ImageField(upload_to='blog_img')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('release_date', models.DateTimeField(verbose_name='date released')),
                ('img', models.ImageField(upload_to='product_img')),
                ('list_price', models.FloatField(blank=True, default=None, null=True)),
                ('discount', models.FloatField(default=0)),
                ('on_sale', models.BooleanField(default=False)),
                ('product_description', models.TextField(max_length=200)),
                ('brand', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.brand')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=100)),
                ('shop_section', models.CharField(choices=[('Electronics', 'Electronics'), ('Fashion', 'Fashion'), ('Grocery', 'Grocery')], max_length=50)),
                ('img', models.ImageField(default='noimg.png', null=True, upload_to='product_category')),
                ('display', models.BooleanField(default=True)),
                ('category_description', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='slider_img')),
                ('display', models.BooleanField(default=False)),
                ('link', models.CharField(max_length=255)),
                ('slider_description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_rate', models.FloatField(default=0)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.productcategory'),
        ),
    ]
