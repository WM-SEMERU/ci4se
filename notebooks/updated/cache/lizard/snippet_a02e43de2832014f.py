def transpose(attrs, inputs, proto_obj):
    new_attrs = translation_utils._fix_attribute_names(attrs, {'perm': 'axes'})
    return 'transpose', new_attrs, inputs