# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-26 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Категории')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Наименование')),
                ('image', models.ImageField(upload_to='image')),
                ('description', models.TextField(max_length=150, verbose_name='Описание')),
                ('coast', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('quantity', models.IntegerField(verbose_name='Колличество')),
                ('code', models.CharField(max_length=50, verbose_name='Код товара')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='katalog.Categories')),
            ],
        ),
    ]
