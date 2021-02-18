from django.db import models

class Dish(models.Model):
    title = models.CharField(max_length=100,verbose_name="название блюда", help_text='напишите название блюда')
    dish_type = models.CharField(max_length=100, verbose_name='тип блюда')
    description = models.CharField(max_length=500, verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блюда'
        verbose_name_plural = 'блюда'
        # вербоз плурал это множ
class Drinks(models.Model):
    title = models.CharField(max_length=100,verbose_name="название напитки", help_text='напишите название напитки')
    dish_type = models.CharField(max_length=100, verbose_name='тип ')
    description = models.CharField(max_length=500, verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Напитки'
        verbose_name_plural = 'Напитки'