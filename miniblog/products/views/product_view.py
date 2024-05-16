from django.shortcuts import redirect, render

from products.repositories.category import CategoryRepository
from products.repositories.products import ProductRepository

repo = ProductRepository()
repoCat = CategoryRepository()


def index_view(request):
    return render(
        request,
        "index/index.html",
    )


def product_list(request):
    products = repo.get_all()
    return render(
        request,
        "products/list.html",
        dict(products=products),
    )


def product_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        stock = request.POST.get("stock")
        id_category = request.POST.get("id_category")
        category = repoCat.get_by_id(id=id_category)

        producto_nuevo = repo.create(
            nombre=name,
            descripcion=description,
            precio=float(price),
            stock=stock,
            categoria=category,
        )
        return redirect("products_detail", producto_nuevo.id)

    categorias = repoCat.get_all()
    return render(
        request,
        "products/create.html",
        dict(categories=categorias),
    )


def product_detail(request, id):
    producto = repo.get_by_id(id=id)
    return render(
        request,
        "products/detail.html",
        dict(product=producto),
    )


def product_update(request, id):
    product = repo.get_by_id(id=id)
    categorias = repoCat.get_all()

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        stock = request.POST.get("stock")
        id_category = request.POST.get("id_category")
        category = repoCat.get_by_id(id=id_category)

        repo.update(
            producto=product,
            nombre=name,
            descripcion=description,
            precio=float(price),
            stock=stock,
            categoria=category,
        )
        return redirect("category_list", product.id)

    return render(
        request,
        "products/update.html",
        dict(
            categories=categorias,
            product=product,
        ),
    )


def product_delete(request, id):
    producto = repo.get_by_id(id)
    repo.delete(producto=producto)
    return redirect("products_list")
