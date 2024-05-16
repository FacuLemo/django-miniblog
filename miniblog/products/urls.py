from django.urls import path

from products.views.product_view import (
    product_create,
    product_delete,
    product_detail,
    product_list,
    product_update,
)

urlpatterns = [
    path(
        "",
        view=product_list,
        name="products_list",
    ),
    path(
        "create/",
        view=product_create,
        name="products_create",
    ),
    path(
        "<int:id>/",
        view=product_detail,
        name="products_detail",
    ),
    path(
        "<int:id>/update",
        view=product_update,
        name="products_update",
    ),
    path(
        "<int:id>/delete",
        view=product_delete,
        name="products_delete",
    ),
    # categorías
]
