def _convert_hbf_meta_val_for_xml(key, val):
    if isinstance(val, list):
        return [_convert_hbf_meta_val_for_xml(key, i) for i in val]
    is_literal = True
    content = None
    if isinstance(val, dict):
        ret = val
        if '@href' in val:
            is_literal = False
        else:
            content = val.get('$')
            if isinstance(content, dict) and _contains_hbf_meta_keys(val):
                is_literal = False
    else:
        ret = {}
        content = val
    if is_literal:
        ret.setdefault('@xsi:type', 'nex:LiteralMeta')
        ret.setdefault('@property', key)
        if content is not None:
            ret.setdefault('@datatype',
                _python_instance_to_nexml_meta_datatype(content))
        if ret is not val:
            ret['$'] = content
    else:
        ret.setdefault('@xsi:type', 'nex:ResourceMeta')
        ret.setdefault('@rel', key)
    return ret