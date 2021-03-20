from django.db import models
from utils.constants import TYPE, TYPE_BULLET

# Create your models here.


class BookJournalBase(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    created_at = models.DateField(verbose_name='Дата публикации')
    description = models.TextField(max_length=500, blank=True, verbose_name="Описание")

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Книга-Журнал'
        verbose_name_plural = 'Книги-Журналы'
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField(default=0, verbose_name='Количество страниц')
    genre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Жанр')

    class Meta:
        ordering = ['num_pages']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Journal(BookJournalBase):
    publisher = models.CharField(max_length=255, null=True, blank=True, verbose_name='Издатель')
    type = models.CharField(max_length=255, choices=TYPE, default=TYPE_BULLET, verbose_name='Типы')

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'
