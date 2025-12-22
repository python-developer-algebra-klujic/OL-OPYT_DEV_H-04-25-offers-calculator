from decimal import Decimal
from django.db import models


class Ingredient(models.Model):
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

    def __str__(self):
        if self.name != '' and self.code != '':
            return f'{self.name} ({self.code})'
        else:
            return f'{self.name}'

    class Meta:
        ordering = ['name', 'code']

    def calculate_total_price(self):
        self.total_price = Decimal(self.base_price) * Decimal(self.price_modificator)

    def save(self, *args, **kwargs):
        self.calculate_total_price()
        super(Ingredient, self).save(*args, **kwargs)
