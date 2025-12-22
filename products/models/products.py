from decimal import Decimal
from django.db import models

from .ingredients import Ingredient


class Product(models.Model):
    name = models.CharField(max_length=150,
                            null=False,
                            blank=False,
                            help_text='Naziv sastojka')
    code = models.CharField(max_length=15,
                            null=False,
                            blank=False,
                            help_text='Šifra sastojka')
    description = models.TextField(max_length=750,
                                   null=False,
                                   blank=False,
                                   help_text='Opis sastojka')
    base_price = models.DecimalField(max_digits=18,
                                     decimal_places=6,
                                     default=Decimal('0.00'),
                                     null=False,
                                     blank=True,
                                     help_text='Osnovna cijena sastojka')
    price_modificator = models.DecimalField(max_digits=5,
                                            decimal_places=3,
                                            default=Decimal('1.00'),
                                            null=False,
                                            blank=True,
                                            help_text='Modifikator cijene')
    total_price = models.DecimalField(max_digits=18,
                                      decimal_places=3,
                                      default=Decimal('0.00'),
                                      null=True,
                                      blank=True,
                                      help_text='Ukupna cijena sastojka')

    ingredients = models.ManyToManyField(Ingredient,
                                         related_name='products',
                                         blank=True)

    ingredients_from_products = models.ManyToManyField('Product',
                                                       blank=True)

    def __str__(self):
        if self.name != '' and self.code != '':
            return f'{self.name} ({self.code})'
        else:
            return f'{self.name}'

    class Meta:
        ordering = ['name', 'code']


    def calculate_total_price(self):
        # Zbrojiti sve cijene sastojaka
        # ingredients_total_price = Decimal('0')
        # for ingredient in self.ingredients:
        #     ingredients_total_price += Decimal(ingredient.total_price)
        if len(self.ingredients.all()) > 0:
            ingredients_total_price = Decimal(sum(Decimal(ingredient.total_price) for ingredient in self.ingredients.all()))
        else:
            ingredients_total_price = Decimal(0.0)

        # Zbrojiti sve cijena proizvoda koji su sastojak
        if len(self.ingredients_from_products.all()) > 0:
            ingredient_from_products_total_price = Decimal(sum(Decimal(ingredient_fp.total_price) for ingredient_fp in self.ingredients_from_products.all()))
        else:
            ingredient_from_products_total_price = Decimal(0.0)

        self.base_price = ingredients_total_price + ingredient_from_products_total_price
        self.total_price = Decimal(self.base_price) * Decimal(self.price_modificator)

    def save(self, *args, **kwargs):
        if not self.pk:
            super(Product, self).save(*args, **kwargs)
            self.calculate_total_price()
        else:
            self.calculate_total_price()
            super(Product, self).save(*args, **kwargs)
