from django.contrib import admin
from django.urls import (
    include,
    path,
)

from products.views import category_list, index_view

urlpatterns = [
    path("", index_view, name="index"),
    path("admin/", admin.site.urls),
    path("products/", include("products.urls")),
    path(
        "categories/",
        view=category_list,
        name="category_list",
    ),
]
