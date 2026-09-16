def set_attribute_label(span, resource_type, resource_labels, attribute_key,
    canonical_key=None, label_value_prefix=''):
    if attribute_key in resource_labels:
        if canonical_key is None:
            canonical_key = attribute_key
        pair = {(RESOURCE_LABEL % (resource_type, canonical_key)): 
            label_value_prefix + resource_labels[attribute_key]}
        pair_attrs = Attributes(pair).format_attributes_json().get(
            'attributeMap')
        _update_attr_map(span, pair_attrs)