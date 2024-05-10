from django.contrib import admin
from django.urls import (
    include,
    path,
)

from products.views import (
    category_create,
    category_delete,
    category_list,
    category_update,
    index_view,
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
]
