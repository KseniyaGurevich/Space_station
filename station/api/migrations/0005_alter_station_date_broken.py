# Generated by Django 3.2.16 on 2022-11-30 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_station_date_broken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='date_broken',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата поломки'),
        ),
    ]
