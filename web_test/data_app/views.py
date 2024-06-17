import os
from django.shortcuts import render, redirect, HttpResponse

from web_test.data_app.servers import product_list_server
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

""" def update(request):
    # 指定搜索文件的根目录
    root_dir = r'D:\workspace\Current project\Art data view\web_test\static\img'
    # 找出所有的货号
    products = Product.objects.all()

    # 遍历所有货号
    for product in tqdm(products):
        product_code = product.product_code

        # 初始化找到的文件名
        found_file_path = None

        # 遍历目录及其子目录
        for subdir, _, files in os.walk(root_dir):
            
            for file in files:
                #print(file)
                if product_code in file:
                    found_file_path = os.path.join(subdir, file)
                    break
            if found_file_path:
                break

        # 如果找到对应的文件名，则更新图片路径
        if found_file_path:
            # 获取相对于 static 目录的路径
            relative_path = found_file_path.split('static')[-1]
            product.img_path = relative_path
            product.save()

    #return render(request, 'update_image_paths.html', {'products': products})
    #return redirect("/")
    return HttpResponse("更新成功") """