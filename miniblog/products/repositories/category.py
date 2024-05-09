from typing import List, Optional

from products.models import Category


class CategoryRepository:

    def get_all(self) -> List[Category]:
        return Category.objects.all()

    def filter_by_id(self, id: int) -> Optional[Category]:
        return Category.objects.filter(id=id).first()

    def get_by_id(self, id: int) -> Optional[Category]:
        try:
            cat = Category.objects.get(id=id)
        except ():
            cat = None
        return cat

    def create(self, nombre: str):
        return Category.objects.create(
            name=nombre,
        )

    def delete(self, categoria: Category):
        return categoria.delete()

    def update(
        self,
        categoria: Category,
        nombre: str,
    ) -> Category:
        categoria.name = nombre
        categoria.save()
