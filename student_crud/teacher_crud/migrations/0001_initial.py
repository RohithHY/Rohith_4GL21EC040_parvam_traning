# Generated by Django 4.2 on 2025-03-25 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('teaher_id', models.IntegerField(max_length=20, unique=True)),
                ('qualification', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=50)),
            ],
        ),
    ]
