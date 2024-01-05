# Generated by Django 5.0 on 2023-12-20 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('class1', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('regno', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('Value', models.IntegerField()),
                ('user_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('Value', models.IntegerField()),
                ('user_type', models.CharField(max_length=10)),
            ],
        ),
    ]