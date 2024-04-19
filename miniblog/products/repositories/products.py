from typing import List, Optional

from products.models import Category, Product


class ProductRepository:
    def create(
        self,
        nombre,
        precio,
        cantidad,
        descripcion: Optional[str] = None,
        categoria: Optional[Category] = None,
    ) -> Product.objects:
        return Product.objects.create(
            name=nombre,
            description=descripcion,
            price=precio,
            stock=cantidad,
            category=categoria,
        )

    def get_all(self) -> List[Product]:
        return Product.objects.all()

    # este todavía no lo probé pero debería andar.
    def get_by_id(self, p_id: int) -> Optional[Product]:
        try:
            p = Product.objects.filter(id=p_id).first()
            return p
        except ():
            return print("no existe producto con ese id")

    def get_by_price_range(
        self,
        min_price: int,
        max_price: int,
    ) -> Optional[Product]:
        return Product.objects.filter(
            price__range=(min_price, max_price),
        )

    def get_by_category_id(self, category_id: int) -> Optional[Product]:
        try:
            p = Category.objects.filter(id=category_id).first()
            return p
        except ():
            return print("no existe producto con esa categoría id")
