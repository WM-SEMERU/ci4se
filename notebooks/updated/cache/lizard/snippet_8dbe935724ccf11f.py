def _index_filter(index_data, filter_value, filter_operator,
    field_converter=None):
    filtered_data = []
    if filter_operator == operator.eq:
        if field_converter is not None:
            filter_value = field_converter(filter_value)
        filtered_data = index_data.get(filter_value)
    else:
        for field, data_obj_list in index_data.items():
            if field_converter is not None:
                field = field_converter(field)
            if filter_operator(field, filter_value):
                filtered_data.extend(data_obj_list)
    return filtered_data