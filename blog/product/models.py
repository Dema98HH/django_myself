from django.db import models





class Brand(models.Model):
    brand_name = models.CharField(max_length=100)

    def __str__ (self):
        return f"Brand: {self.brand_name}"


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.ForeignKey(
        "Brand",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    price = models.DecimalField(decimal_places=2, max_digits=6)
    _quantity = models.PositiveSmallIntegerField(blank=False)
    _sold = models.PositiveSmallIntegerField(blank=True)

    @property
    def quantity(self):
        return self._quantity

    @property
    def sold(self):
        return self.sold

    @quantity.setter
    def quantity(self, value):
        self._quantity += value

    @sold.setter
    def sold(self, value):
        self._sold += value

    def __str__ (self):
        return f"Product: {self.product_name} ({self.brand.brand_name})"