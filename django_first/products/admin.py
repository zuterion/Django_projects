from django.contrib import admin
from .models import ProductLine
# Register your models here.

class ProductLineAdmin(admin.ModelAdmin):
    list_display=("productLine","textDescription","htmlDescription")


admin.site.register(ProductLine,ProductLineAdmin)