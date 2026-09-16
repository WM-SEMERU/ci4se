def dict_key_tag(Class, key, namespaces=None):
    namespaces = namespaces or Class.NS
    ns = Class.tag_namespace(key)
    tag = Class.tag_name(key)
    if ns is None and ':' in key:
        prefix, tag = key.split(':')
        if prefix in namespaces.keys():
            ns = namespaces[prefix]
    if ns is not None:
        tag = '{%s}%s' % (ns, tag)
    return tag