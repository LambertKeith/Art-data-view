import os
from django.shortcuts import render, redirect, HttpResponse
from .models import Product
from django.core.paginator import Paginator
from .update_server.get_data_from_single_table import update as update_from_table



def product_list(request):
    """显示商品列表"""
    products = Product.objects.all()
    filters = {}

    # 获取所有查询参数
    query_params = request.GET.copy()

    # 获取每页显示的条数，默认为20
    per_page = request.GET.get('per_page', 20)
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 20  # 如果转换失败，使用默认值

    # 获取排序字段和顺序
    sort_by = request.GET.get('sort', 'id')  # 默认按 'id' 排序
    order = request.GET.get('order', 'asc')  # 默认升序排序

    # 确定排序方式
    if order == 'asc':
        sort_field = sort_by
    else:
        sort_field = '-' + sort_by

    # 移除分页和每页显示条数参数
    query_params.pop('page', None)
    query_params.pop('per_page', None)
    query_params.pop('sort', None)
    query_params.pop('order', None)

    # 应用过滤条件
    for key, value in query_params.items():
        if value:
            filters[key + '__icontains'] = value

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