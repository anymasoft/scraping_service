from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Город')
    slug = models.CharField(max_length=50, blank=True, verbose_name='Слаг')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


