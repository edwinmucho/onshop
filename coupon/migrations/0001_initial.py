# Generated by Django 2.0 on 2019-07-28 09:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('use_from', models.DateTimeField()),
                ('use_to', models.DateTimeField()),
                ('amount', models.IntegerField(validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(10000)])),
                ('active', models.BooleanField()),
            ],
        ),
    ]
