from django.db import models

class Dish(models.Model):
    title = models.CharField(max_length=100,verbose_name="название хавчика", help_text='название блюда пиши')
    dish_type = models.CharField(max_length=100, verbose_name='че за хавчик')
    description = models.CharField(max_length=500, verbose_name='из чего хочешь?')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блюда'
        # вербоз это единственное число
        verbose_name_plural = 'блюда'
        # вербоз плурал это множ число