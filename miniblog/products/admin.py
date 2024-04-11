from django.contrib import admin

from products.models import (
    Category,
    Product,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ("name", "price")  # puede ser tupla o lista.
    search_fields = ("name", "price")
    # list_filter = ("category",)
    list_editable = ("price",)
    empty_value_display = "No hay datos para este campo"

    list_display = (
        "name",
        "price",
        "description",
        "category",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
