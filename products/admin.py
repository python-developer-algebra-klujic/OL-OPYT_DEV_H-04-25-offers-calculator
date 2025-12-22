from django.contrib import admin

from products.models import Ingredient, Product


admin.site.register([Ingredient, Product])
