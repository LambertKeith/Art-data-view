from .models import Product
from django.contrib import admin

@admin.register(Product)
class ArtTestAdmin(admin.ModelAdmin):
    list_display = (
        'img_path', 'product_code', 'original_product_code', 'style_code', 'factory_code', 
        'factory_product_code', 'insole_material', 'outsole_material', 
        'lining_material', 'upper_material', 'group', 'platform', 'cost', 
        'product_name', 'season_classification', 'season', 'category', 
        'first_order_date', 'vip_first_sale_date', 'dew_first_sale_date', 
        'latest_status', 'original_status'
    )  # 列表显示的字段
    
    search_fields = (
        'product_code', 'original_product_code', 'style_code', 'factory_code', 
        'factory_product_code', 'insole_material', 'outsole_material', 
        'lining_material', 'upper_material', 'group', 'platform', 
        'product_name', 'season_classification', 'season', 'category', 
        'first_order_date', 'vip_first_sale_date', 'dew_first_sale_date', 
        'latest_status', 'original_status'
    )  # 搜索框可搜索的字段
    
    list_filter = (
        'group', 'platform', 'cost', 'season_classification', 'season', 'category', 
        'first_order_date', 'vip_first_sale_date', 'dew_first_sale_date', 
        'latest_status', 'original_status'
    )  # 过滤器可筛选的字段