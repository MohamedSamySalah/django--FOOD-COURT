# Generated by Django 4.0.4 on 2022-05-13 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dishes', '0002_dishes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resturants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Restaurant_name', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=5)),
                ('R_Description', models.TextField(max_length=50)),
            ],
        ),
    ]