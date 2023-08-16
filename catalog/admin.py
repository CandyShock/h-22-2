from django.contrib import admin

from catalog.models import Product, Category, Version


# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomination', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('nomination', 'description')


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomination')
    list_filter = ('nomination',)
    search_fields = ('nomination', 'description')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'version_number', 'name_version')
    list_filter = ('version_number',)