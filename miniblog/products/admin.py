from django.contrib import admin
from django.utils.html import format_html

from products.models import (
    Category,
    Product,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ("name", "price")  # puede ser tupla o lista.
    search_fields = ("name", "price")
    list_filter = ("category",)
    # list_editable = ("price",)
    readonly_fields = ("name",)
    empty_value_display = "No hay datos para este campo"

    list_display = (
        "name",
        "price",
        "get_stock",
        "description",
        "category",
        "get_price_range",
        "get_total",
    )
    fieldsets = [
        (
            "informacion de producto",
            {
                "fields": [
                    "name",
                    "price",
                ]
            },
        ),
        (
            "mas info del producto",
            {
                "classes": ["collapse"],
                "fields": [
                    "description",
                    "stock",
                ],
            },
        ),
    ]

    def get_total(self, obj):  # recibe el obj del admin
        return obj.price * obj.stock  # ejemplo xd esto iría en venta por ej

    def get_stock(self, obj):
        POCO = "#FF0000"
        BIEN = "#00FF00"
        DEMACIADO = "#FFD300"
        if obj.stock < 10:
            codigo = POCO
        if 10 < obj.stock < 25:
            codigo = BIEN
        if obj.stock >= 25:
            codigo = DEMACIADO
        return format_html(
            f'<span style="color:{codigo}">{obj.stock}</span>',
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
