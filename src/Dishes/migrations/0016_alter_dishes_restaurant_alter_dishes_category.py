# Generated by Django 4.0.4 on 2022-05-26 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dishes', '0015_rename_restaurant_dishes_dishes_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='Restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Restaurant_dishes', to='Dishes.resturants'),
        ),
        migrations.AlterField(
            model_name='dishes',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category_dishes', to='Dishes.category'),
        ),
    ]
