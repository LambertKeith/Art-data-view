import os
from django.shortcuts import render, redirect, HttpResponse
from .models import Product
from django.core.paginator import Paginator



def product_list(request):
    """显示商品列表

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """    
    products = Product.objects.all().order_by('id')  # 按照主键排序
    filters = {}
    
    # 获取所有查询参数
    query_params = request.GET.copy()
    
    # 移除分页参数
    query_params.pop('page', None)

    # 应用过滤条件
    for key, value in query_params.items():
        if value:
            filters[key + '__icontains'] = value
    
    if filters:
        products = products.filter(**filters).order_by('id')  # 保持排序

    # 添加分页功能，每页显示10条数据
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'filters': query_params,
    }
    
    return render(request, 'product_list.html', context)


def update(request):
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