# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True, help_text='Unique value for product page URL, created from name.')),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('meta_keywords', models.CharField(max_length=255, verbose_name='Meta Keywords', help_text=' Comma-delimited set of SEO keywords for meta tag')),
                ('meta_description', models.CharField(max_length=255, verbose_name='Meta Description', help_text='Content for description meta tag')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'categories',
                'verbose_name_plural': 'Categories',
                'ordering': ['-created_at'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True, help_text='Unique value for product page URL, created from name.')),
                ('brand', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('old_price', models.DecimalField(decimal_places=2, blank=True, max_digits=9, default=0.0)),
                ('image', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('meta_keywords', models.CharField(max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')),
                ('meta_description', models.CharField(max_length=255, help_text='Content for description meta tag')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='catalogue.Category')),
            ],
            options={
                'db_table': 'products',
                'ordering': ['-created_at'],
            },
            bases=(models.Model,),
        ),
    ]
