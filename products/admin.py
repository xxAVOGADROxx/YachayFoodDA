from django.contrib import admin

# Register your models here.
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductoAdmin(admin.ModelAdmin):
	list_display= ['name', 'image','description', 'stock', 'delivery_date','limit_date','register_date'	]
	list_filter = ['delivery_date','register_date']
	search_fields = ('name','id_Product')#realizar el cambio al nombre del author
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductoAdmin)
