# Generated by Django 5.1.5 on 2025-05-05 04:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='franchises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='studios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='studios/picture/')),
            ],
        ),
        migrations.CreateModel(
            name='types_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_name', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('trailer', models.URLField()),
                ('releaseYear', models.DateField()),
                ('review', models.FloatField(default=0.0)),
                ('description', models.CharField(max_length=375)),
                ('portraitImage', models.ImageField(upload_to='anime/portraitImage/')),
                ('franchise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.franchises')),
                ('genres', models.ManyToManyField(to='main.genres')),
                ('studio', models.ManyToManyField(to='main.studios')),
                ('type_field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.types_model')),
            ],
        ),
    ]
