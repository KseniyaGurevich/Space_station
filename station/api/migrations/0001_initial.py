# Generated by Django 3.2.16 on 2022-11-30 21:59

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
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Название станции')),
                ('state', models.CharField(choices=[('running', 'Работает'), ('broken', 'Сломана')], default='running', max_length=30, verbose_name='Состояние')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_broken', models.DateTimeField(default=0, verbose_name='Дата поломки')),
                ('x', models.IntegerField(default=100, verbose_name='Координата x')),
                ('y', models.IntegerField(default=100, verbose_name='Координата y')),
                ('z', models.IntegerField(default=100, verbose_name='Координата z')),
            ],
            options={
                'verbose_name': 'Станция',
                'verbose_name_plural': 'Станции',
            },
        ),
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('axis', models.CharField(choices=[('x', 'x'), ('y', 'y'), ('z', 'z')], max_length=5, verbose_name='Ось')),
                ('distance', models.IntegerField(verbose_name='Расстояние')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, который создал указание')),
            ],
            options={
                'verbose_name': 'Состояние',
                'verbose_name_plural': 'Состояния',
            },
        ),
    ]
