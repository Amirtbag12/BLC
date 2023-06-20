from django.contrib import admin
from .models import Cart, Comparison

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_title', 'quantity', 'price', 'image', 'color')
    list_filter = ('user',)
    search_fields = ('user', 'product_title')

admin.site.register(Cart, CartAdmin)

class ComparisonAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_title1','product_title2',)
    search_fields = ('user',)

admin.site.register(Comparison, ComparisonAdmin)