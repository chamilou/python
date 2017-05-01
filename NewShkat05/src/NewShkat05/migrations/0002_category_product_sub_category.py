# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewShkat05', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(help_text='Unique value for product page URL, created from name.', unique=True)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('meta_keywords', models.CharField(help_text=' Comma-delimited set of SEO keywords for meta tag', verbose_name='Meta Keywords', max_length=255)),
                ('meta_description', models.CharField(help_text='Content for description meta tag', verbose_name='Meta Description', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Category',
                'ordering': ['-created_at'],
                'db_table': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(help_text='Unique value for product page URL, created from name.', unique=True, max_length=255)),
                ('brand', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=50)),
                ('price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('old_price', models.DecimalField(default=0.0, blank=True, max_digits=9, decimal_places=2)),
                ('image', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(verbose_name='Description')),
                ('meta_keywords', models.CharField(help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255)),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='NewShkat05.Category')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'products',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SUB_Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(help_text='Unique value for product page URL, created from name.', unique=True)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('meta_keywords', models.CharField(help_text=' Comma-delimited set of SEO keywords for meta tag', verbose_name='Meta Keywords', max_length=255)),
                ('meta_description', models.CharField(help_text='Content for description meta tag', verbose_name='Meta Description', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='NewShkat05.Category')),
            ],
            options={
                'verbose_name_plural': 'SUB_Category',
                'ordering': ['-created_at'],
                'db_table': 'sub_categories',
            },
            bases=(models.Model,),
        ),
    ]
