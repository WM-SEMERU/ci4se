def batch_norm(attrs, inputs, proto_obj):
    new_attrs = translation_utils._fix_attribute_names(attrs, {'epsilon':
        'eps', 'is_test': 'fix_gamma'})
    new_attrs = translation_utils._remove_attributes(new_attrs, ['spatial',
        'consumed_inputs'])
    cudnn_min_eps = 1e-05
    cudnn_off = 0 if attrs.get('epsilon', cudnn_min_eps
        ) >= cudnn_min_eps else 1
    new_attrs = translation_utils._add_extra_attributes(new_attrs, {
        'cudnn_off': cudnn_off})
    new_attrs['fix_gamma'] = not attrs.get('is_test', 1)
    return 'BatchNorm', new_attrs, inputs