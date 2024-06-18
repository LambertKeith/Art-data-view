import os
from django.shortcuts import render, redirect, HttpResponse

from .servers import product_list_server
from .models import Product
from django.core.paginator import Paginator
from .update_server.get_data_from_single_table import update as update_from_table



def product_list(request):
    """显示商品列表"""
    products = Product.objects.all()

    # 获取每页显示的条数
    per_page = product_list_server.get_per_page(request)

    # 获取排序字段和顺序
    sort_by, order, sort_field = product_list_server.get_sorting_params(request)

    # 获取过滤条件
    filters, query_params = product_list_server.get_filters(request)
    if filters:
        products = products.filter(**filters)

    products = products.order_by(sort_field)

    # 添加分页功能
    paginator = Paginator(products, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'filters': query_params,
        'per_page': per_page,
        'current_sort': sort_by,
        'current_order': order,
    }

    return render(request, 'product_list.html', context)


def update(request):
    return update_from_table(request)
    return redirect("/")


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def save_product_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('id')
        field = data.get('field')
        value = data.get('value')

        try:
            product = Product.objects.get(id=product_id)
            setattr(product, field, value)
            product.save()
            return JsonResponse({'success': True})
        except Product.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Product not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
