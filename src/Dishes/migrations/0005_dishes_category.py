# Generated by Django 4.0.4 on 2022-05-13 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dishes', '0004_alter_category_name_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishes',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Dishes.category'),
            preserve_default=False,
        ),
    ]
