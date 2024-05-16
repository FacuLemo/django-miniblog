from typing import List, Optional

# name = models.CharField(max_length=200)
# address = models.TextField()
# phone = models.CharField(max_length=15)
from products.models import Supplier


class SupplierRepository:

    def get_all(self) -> List[Supplier]:
        return Supplier.objects.all()

    def filter_by_id(self, id: int) -> Optional[Supplier]:
        return Supplier.objects.filter(id=id).first()

    def get_by_id(self, id: int) -> Optional[Supplier]:
        try:
            sup = Supplier.objects.get(id=id)
        except ():
            sup = None
        return sup

    def create(
        self,
        nombre: str,
        direccion: str,
        telefono: str,
    ):
        return Supplier.objects.create(
            name=nombre,
            address=direccion,
            phone=telefono,
        )

    def delete(self, supplier: Supplier):
        return supplier.delete()

    def update(
        self,
        supplier: Supplier,
        nombre: str,
        direccion: str,
        telefono: str,
    ) -> Supplier:
        supplier.name = nombre
        supplier.address = direccion
        supplier.phone = telefono
        supplier.save()
