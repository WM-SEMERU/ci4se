def depthtospace(attrs, inputs, proto_obj):
    new_attrs = translation_utils._fix_attribute_names(attrs, {'blocksize':
        'block_size'})
    return 'depth_to_space', new_attrs, inputs