def getTypeOrd(orderby_item):
    if 'item' not in orderby_item:
        return 0
    val = orderby_item['item']
    if val is None:
        return 1
    if isinstance(val, bool):
        return 2
    if isinstance(val, numbers.Number):
        return 4
    if isinstance(val, six.string_types):
        return 5
    raise TypeError('unknown type' + str(val))