def convert_kv(key, val, attr_type, attr={}, cdata=False):
    LOG.info('Inside convert_kv(): key="%s", val="%s", type(val) is: "%s"' %
        (unicode_me(key), unicode_me(val), type(val).__name__))
    key, attr = make_valid_xml_name(key, attr)
    if attr_type:
        attr['type'] = get_xml_type(val)
    attrstring = make_attrstring(attr)
    return '<%s%s>%s</%s>' % (key, attrstring, wrap_cdata(val) if cdata ==
        True else escape_xml(val), key)