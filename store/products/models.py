from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    #Данное наследование показывает нам, что данное поле в БД будет иметь тип данных чарфилд
    name = models.CharField(max_length=256, unique=True)
    #Отличие чарфилда от текстфилда в том, что етксфилд принимамет в себя большое количество текста
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=9999, decimal_places=9)
    #Количество товаров на складе
    quontity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name