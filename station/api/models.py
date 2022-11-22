from django.contrib.auth import get_user_model
from django.db import models


CHOICES = (
    ('running', 'Работает'),
    ('broken', 'Сломана')
)

User = get_user_model()


class Station(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Название станции'
    )
    state = models.CharField(
        default='running',
        choices=CHOICES, max_length=30,
        verbose_name='Состояние'
    )
    date_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    date_broken = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата поломки'
    )

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'

    def __str__(self):
        return f'{self.name}'


class Instructions(models.Model):
    # station = models.ForeignKey(
    #     Station,
    #     on_delete=models.CASCADE,
    #     related_name='instruction',
    #     verbose_name='Название станции'
    # )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь, который создал указание'
    )
    axis = models.CharField(
        max_length=50,
        verbose_name='Координаты'
    )
    distance = models.IntegerField(
        verbose_name='Пройденное расстояние'
    )

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'

    def __str__(self):
        return f'{self.axis}'


class StationInstruction(models.Model):
    station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name='station',
        verbose_name='Название станции'
    )
    instruction = models.ForeignKey(
        Instructions,
        on_delete=models.CASCADE,
        related_name='instruction',
        verbose_name='Смещение'
    )

    class Meta:
        verbose_name = 'Инструкция для станции'
        verbose_name_plural = 'Инструкции для станций'


