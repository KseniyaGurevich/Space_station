from django.contrib.auth import get_user_model
from django.db import models


CHOICES = (
    ('running', 'Работает'),
    ('broken', 'Сломана')
)

AXIS = (
    ('x', 'x'),
    ('y', 'y'),
    ('z', 'z')
)


User = get_user_model()


class Instructions(models.Model):
    """Указание для движения станции"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь, который создал указание'
    )
    axis = models.CharField(
        max_length=5,
        choices=AXIS,
     )
    distance = models.IntegerField(
        verbose_name='Пройденное расстояние'
    )

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'

    def __str__(self):
        return f'{self.axis}={self.distance}'


class Station(models.Model):
    """Станция"""
    name = models.CharField(
        max_length=30,
        verbose_name='Название станции',
        unique=True,
    )
    state = models.CharField(
        default='running',
        choices=CHOICES,
        max_length=30,
        verbose_name='Состояние'
    )
    date_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    date_broken = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата поломки'
    )
    x = models.IntegerField(default=100)
    y = models.IntegerField(default=100)
    z = models.IntegerField(default=100)

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'

    def __str__(self):
        return f'{self.name}'
