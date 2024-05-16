from django.shortcuts import redirect, render

from products.repositories.suppliers import SupplierRepository

repoSup = SupplierRepository()


def supplier_list(request):
    suppliers = repoSup.get_all()
    return render(
        request,
        "suppliers/list.html",
        dict(suppliers=suppliers),
    )


def supplier_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        repoSup.create(nombre=name)
        return redirect("supplier_list")
    return render(
        request,
        "suppliers/create.html",
    )


def supplier_delete(request, id):
    supp = repoSup.get_by_id(id)
    repoSup.delete(supplier=supp)
    return redirect("supplier_list")


def supplier_update(request, id):
    supp = repoSup.get_by_id(id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        repoSup.update(categoria=supp, nombre=name)
        return redirect("supplier_list")

    return render(
        request,
        "suppliers/update.html",
        dict(
            supplier=supp,
        ),
    )
