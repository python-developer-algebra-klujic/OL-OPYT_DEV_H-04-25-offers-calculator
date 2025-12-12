from decimal import Decimal
from django.db import models

# Create your models here.
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
                                     help_text='Osnovna cijena')

    class Meta:
        ordering = ['name', 'code']
