def enumerate(context, data):
    items = ensure_list(context.params.get('items'))
    for item in items:
        data['item'] = item
        context.emit(data=data)