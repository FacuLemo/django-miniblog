from django.shortcuts import redirect, render

from products.repositories.category import CategoryRepository

repoCat = CategoryRepository()


def category_list(request):
    categories = repoCat.get_all()
    return render(
        request,
        "categories/list.html",
        dict(categories=categories),
    )


def category_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        repoCat.create(nombre=name)
        return redirect("category_list")
    return render(
        request,
        "categories/create.html",
    )


def category_delete(request, id):
    categ = repoCat.get_by_id(id)
    repoCat.delete(categoria=categ)
    return redirect("category_list")


def category_update(request, id):
    categ = repoCat.get_by_id(id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        repoCat.update(categoria=categ, nombre=name)
        return redirect("category_list")

    return render(
        request,
        "categories/update.html",
        dict(
            category=categ,
        ),
    )
