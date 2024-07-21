from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название книги ')
    author = models.CharField(max_length=100, verbose_name='Имя автора')
    desc = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'книги'
