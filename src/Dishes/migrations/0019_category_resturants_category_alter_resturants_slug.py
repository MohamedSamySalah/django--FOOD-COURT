# Generated by Django 4.0.4 on 2022-05-28 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dishes', '0018_alter_dishes_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Resturants_category',
            field=models.ManyToManyField(blank=True, null=True, to='Dishes.resturants'),
        ),
        migrations.AlterField(
            model_name='resturants',
            name='slug',
            field=models.SlugField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
