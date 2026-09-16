def reduce_sum(attrs, inputs, proto_obj):
    new_attrs = translation_utils._fix_attribute_names(attrs, {'axes': 'axis'})
    return 'sum', new_attrs, inputs