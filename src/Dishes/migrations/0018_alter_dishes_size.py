# Generated by Django 4.0.4 on 2022-05-26 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dishes', '0017_delete_bbb_resturants_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='size',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Double', 'Double'), ('Trible', 'Trible')], max_length=6, null=True),
        ),
    ]
