def get_per_page(request):
    """获取每页显示的条数，默认为20"""
    per_page = request.GET.get('per_page', 20)
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 20  # 如果转换失败，使用默认值
    return per_page

def get_sorting_params(request):
    """获取排序字段和顺序"""
    sort_by = request.GET.get('sort', 'id')  # 默认按 'id' 排序
    order = request.GET.get('order', 'asc')  # 默认升序排序
    sort_field = sort_by if order == 'asc' else '-' + sort_by
    return sort_by, order, sort_field

def get_filters(request):
    """获取过滤条件"""
    query_params = request.GET.copy()
    filters = {}

    # 移除分页和排序参数
    query_params.pop('page', None)
    query_params.pop('per_page', None)
    query_params.pop('sort', None)
    query_params.pop('order', None)

    # 应用过滤条件
    for key, value in query_params.items():
        if value:
            filters[key + '__icontains'] = value

    return filters, query_params