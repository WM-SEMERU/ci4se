def _gen_hbf_el(self, x):
    obj = {}
    el_name = x.nodeName
    assert el_name is not None
    att_container = x.attributes
    ns_obj = {}
    if att_container is not None:
        for i in range(att_container.length):
            attr = att_container.item(i)
            n = attr.name
            t = None
            if n.startswith('xmlns'):
                if n == 'xmlns':
                    t = '$'
                elif n.startswith('xmlns:'):
                    t = n[6:]
            if t is None:
                obj['@' + n] = attr.value
            else:
                ns_obj[t] = attr.value
    if ns_obj:
        obj['@xmlns'] = ns_obj
    x.normalize()
    text_content, ntl = _extract_text_and_child_element_list(x)
    if text_content:
        obj['$'] = text_content
    self._hbf_handle_child_elements(obj, ntl)
    return el_name, obj