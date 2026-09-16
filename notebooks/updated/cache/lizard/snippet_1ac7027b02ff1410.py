def result_list(context):
    view = context['view']
    object_list = context['object_list']
    headers = list(result_headers(view))
    num_sorted_fields = 0
    for h in headers:
        if h['sortable'] and h['sorted']:
            num_sorted_fields += 1
    context.update({'result_headers': headers, 'num_sorted_fields':
        num_sorted_fields, 'results': list(results(view, object_list))})
    return context