# Generated by Django 4.0.4 on 2022-05-28 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dishes', '0024_alter_category_resturants'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name_category',
        ),
        migrations.RemoveField(
            model_name='category',
            name='Resturants',
        ),
        migrations.AddField(
            model_name='category',
            name='Resturants_category',
            field=models.ManyToManyField(blank=True, null=True, to='Dishes.resturants'),
        ),
    ]
