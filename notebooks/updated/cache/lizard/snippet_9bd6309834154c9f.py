def _get_order_by(order, orderby, order_by_fields):
    try:
        db_fieldnames = order_by_fields[orderby]
    except KeyError:
        raise ValueError(
            "Invalid value for 'orderby': '{0}', supported values are: {1}"
            .format(orderby, ', '.join(sorted(order_by_fields.keys()))))
    is_desc = not order and orderby in ORDER_BY_DESC or (order or 'asc').lower(
        ) in ('desc', 'descending')
    if is_desc:
        return map(lambda name: '-' + name, db_fieldnames)
    else:
        return db_fieldnames