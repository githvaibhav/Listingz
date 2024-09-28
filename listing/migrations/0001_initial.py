# Generated by Django 4.2.5 on 2023-10-21 08:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realtor', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('sale_type', models.CharField(choices=[('For Sale', 'for_sale'), ('For Rent', 'for_rent')], default='For Sale', max_length=10)),
                ('home_type', models.CharField(choices=[('House', 'house'), ('Condo', 'condo'), ('Condo', 'condo')], default='House', max_length=10)),
                ('main_photo', models.ImageField(upload_to='listings/')),
                ('photo1', models.ImageField(upload_to='listings/')),
                ('photo2', models.ImageField(upload_to='listings/')),
                ('photo3', models.ImageField(upload_to='listings/')),
                ('is_published', models.BooleanField(default=False)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
