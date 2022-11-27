# Generated by Django 3.2.16 on 2022-11-26 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField(default=100)),
                ('y', models.IntegerField(default=100)),
                ('z', models.IntegerField(default=100)),
            ],
            options={
                'verbose_name': 'Координаты',
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Название станции')),
                ('state', models.CharField(choices=[('running', 'Работает'), ('broken', 'Сломана')], default='running', max_length=30, verbose_name='Состояние')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_broken', models.DateTimeField(blank=True, null=True, verbose_name='Дата поломки')),
            ],
            options={
                'verbose_name': 'Станция',
                'verbose_name_plural': 'Станции',
            },
        ),
        migrations.CreateModel(
            name='StationCoordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.coordinates', verbose_name='Координаты')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station', to='api.station', verbose_name='Название станции')),
            ],
            options={
                'verbose_name': 'Координаты станции',
                'verbose_name_plural': 'Координаты станций',
            },
        ),
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('axis', models.CharField(choices=[('x', 'x'), ('y', 'y'), ('z', 'z')], max_length=5)),
                ('distance', models.IntegerField(verbose_name='Пройденное расстояние')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, который создал указание')),
            ],
            options={
                'verbose_name': 'Состояние',
                'verbose_name_plural': 'Состояния',
            },
        ),
    ]
