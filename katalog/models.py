from django.db import models


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=120, verbose_name="Категории")
    alias = models.SlugField(max_length=120,) #allow_unicode=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, verbose_name="Наименование")
    image = models.ImageField(upload_to="static/img")
    description = models.TextField(max_length=500, verbose_name="Описание")
    coast = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена")
    quantity = models.IntegerField(verbose_name="Колличество")
    code = models.CharField(max_length=50, verbose_name="Код товара")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

