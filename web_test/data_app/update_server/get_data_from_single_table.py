# 直接从现成的精细表中读取

import os
from data_app.models import Product
from tqdm import tqdm
from django.shortcuts import render, redirect, HttpResponse
from web_test.settings import BASE_DIR


def update(request):
    # 指定搜索文件的根目录
    root_dir = rf'{BASE_DIR}\static\img'
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
    return HttpResponse("更新成功") 