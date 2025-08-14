from django.contrib import admin
from .models import MenuItem,Order


# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display('name','price','description')
    search_fields=('name',)
    list_filter('price',)


# Register your models here.
admin.site.register(Item,ItemAdmin)
admin.site.register(MenuItem)