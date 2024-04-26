from django.shortcuts import redirect, render

from products.repositories.products import ProductRepository

repo = ProductRepository()


def product_list(request):
    products = repo.get_all()
    return render(
        request,
        "products/list.html",
        dict(products=products),
    )


def product_create(request): ...


def product_detail(request, id):
    producto = repo.get_by_id(id=id)
    return render(
        request,
        "products/detail.html",
        dict(product=producto),
    )


def product_update(request): ...


def product_delete(request, id):
    producto = repo.get_by_id(id)
    repo.delete(producto=producto)
    return redirect("products_list")
