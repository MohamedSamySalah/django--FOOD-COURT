# Generated by Django 4.0.4 on 2022-05-28 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dishes', '0020_alter_category_resturants_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Resturants_category',
            field=models.ManyToManyField(related_name='Resturants_category', to='Dishes.resturants'),
        ),
    ]
