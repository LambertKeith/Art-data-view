from django.urls import path
from .views import product_list, update, save_product_data

urlpatterns = [
    path('', product_list, name='product_list'),
    path('update/', update, name='update'),
    path('save_product_data/', save_product_data, name='save_product_data'),
]
