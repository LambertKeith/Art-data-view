from .models import Product
from django.contrib import admin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')  # 列表显示的字段
    search_fields = ('name', 'category')  # 搜索框可搜索的字段
    list_filter = ('category', 'price')  # 过滤器可筛选的字段