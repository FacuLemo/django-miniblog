from django.contrib import admin
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.DecimalField(max_digits=6, decimal_places=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    @admin.display(description="Rango de Precios")
    def get_price_range(self):
        if self.price >= 55000:
            return "Alto"
        if 10000 < self.price < 55000:
            return "Medio"
        if self.price <= 10000:
            return "Bajo"

    # def save(self, *args, **kwargs):
    #     if self.price > 0:
    #         super.(self)
    #     else:
    def __str__(self):
        return self.name
