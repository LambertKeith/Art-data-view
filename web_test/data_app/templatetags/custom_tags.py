# myapp/templatetags/custom_tags.py
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def sort_url(context, field):
    request = context['request']
    current_sort = context.get('current_sort', '')
    current_order = context.get('current_order', 'asc')

    if current_sort == field:
        new_order = 'desc' if current_order == 'asc' else 'asc'
    else:
        new_order = 'asc'

    query_params = request.GET.copy()
    query_params['sort'] = field
    query_params['order'] = new_order

    return f"?{query_params.urlencode()}"
