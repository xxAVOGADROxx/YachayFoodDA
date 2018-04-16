# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
                'verbose_name': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('slug', models.SlugField(max_length=200)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('precio_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('limit_date', models.DateTimeField(blank=True, null=True)),
                ('register_date', models.DateField(blank=True, null=True)),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(to='products.Category', related_name='products')),
            ],
            options={
                'managed': True,
                'db_table': 'product',
                'ordering': ('name',),
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
