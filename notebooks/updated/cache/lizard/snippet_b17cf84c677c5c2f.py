def _normalize_cursor(self, cursor, orders):
    if cursor is None:
        return
    if not orders:
        raise ValueError(_NO_ORDERS_FOR_CURSOR)
    document_fields, before = cursor
    order_keys = [order.field.field_path for order in orders]
    if isinstance(document_fields, document.DocumentSnapshot):
        snapshot = document_fields
        document_fields = snapshot.to_dict()
        document_fields['__name__'] = snapshot.reference
    if isinstance(document_fields, dict):
        values = []
        data = document_fields
        for order_key in order_keys:
            try:
                values.append(field_path_module.get_nested_value(order_key,
                    data))
            except KeyError:
                msg = _MISSING_ORDER_BY.format(order_key, data)
                raise ValueError(msg)
        document_fields = values
    if len(document_fields) != len(orders):
        msg = _MISMATCH_CURSOR_W_ORDER_BY.format(document_fields, order_keys)
        raise ValueError(msg)
    _transform_bases = transforms.Sentinel, transforms._ValueList
    for index, key_field in enumerate(zip(order_keys, document_fields)):
        key, field = key_field
        if isinstance(field, _transform_bases):
            msg = _INVALID_CURSOR_TRANSFORM
            raise ValueError(msg)
        if key == '__name__' and isinstance(field, six.string_types):
            document_fields[index] = self._parent.document(field)
    return document_fields, before