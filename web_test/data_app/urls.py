from django.urls import path
from .views import product_list, update

urlpatterns = [
    path('', product_list, name='product_list'),
    path('update/', update, name='update')
]
