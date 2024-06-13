# 直接从现成的精细表中读取

import os
from data_app.models import Product
from tqdm import tqdm
from django.shortcuts import HttpResponse
from web_test.settings import BASE_DIR

def update(request):
    # 指定搜索文件的根目录
    root_dir = os.path.join(BASE_DIR, 'static', 'img')
    static_dir = os.path.join(BASE_DIR, 'static')
    # 找出所有的货号
    products = Product.objects.all()

    # 递归函数来搜索所有子文件夹的内容
    def find_file(root, product_code):
        for subdir, _, files in os.walk(root):
            print(subdir)
            for file in files:
                if product_code in file:
                    return os.path.join(subdir, file)
        return None

    # 遍历所有货号
    for product in tqdm(products):
        product_code = product.original_product_code
        found_file_path = find_file(root_dir, product_code)

        # 如果找到对应的文件名，则更新图片路径
        if found_file_path:
            # 获取相对于 static 目录的路径
            relative_path = os.path.relpath(found_file_path, static_dir)
            product.img_path = '/' + relative_path.replace('\\', '/')
            product.save()

    return HttpResponse("更新成功")

