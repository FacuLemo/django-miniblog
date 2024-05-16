from django.contrib import admin
from django.urls import (
    include,
    path,
)

from products.views.categories_view import (
    category_create,
    category_delete,
    category_list,
    category_update,
)
from products.views.product_view import (
    index_view,
)
from products.views.supplier_view import (
    supplier_create,
    supplier_delete,
    supplier_list,
    supplier_update,
)

urlpatterns = [
    path("", index_view, name="index"),
    path("admin/", admin.site.urls),
    path("products/", include("products.urls")),
    path(
        "categories/",
        view=category_list,
        name="category_list",
    ),
    path(
        "categories/create",
        view=category_create,
        name="category_create",
    ),
    path(
        "categories/<int:id>/delete",
        view=category_delete,
        name="category_delete",
    ),
    path(
        "categories/<int:id>/update",
        view=category_update,
        name="category_update",
    ),
    # Suppliers
    path(
        "suppliers/",
        view=supplier_list,
        name="supplier_list",
    ),
    path(
        "suppliers/create",
        view=supplier_create,
        name="supplier_create",
    ),
    path(
        "suppliers/<int:id>/delete",
        view=supplier_delete,
        name="supplier_delete",
    ),
    path(
        "suppliers/<int:id>/update",
        view=supplier_update,
        name="supplier_update",
    ),
]
