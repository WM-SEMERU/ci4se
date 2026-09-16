def etree_to_dict(t, trim=True, **kw):
    u
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    etree_to_dict_w_args = partial(etree_to_dict, trim=trim, **kw)
    if children:
        dd = defaultdict(list)
        d = {t.tag: {}}
        for dc in map(etree_to_dict_w_args, children):
            for k, v in dc.iteritems():
                if k is not etree.Comment:
                    dd[k].append(v)
        d[t.tag] = {k: (v[0] if len(v) == 1 else v) for k, v in dd.iteritems()}
    if t.attrib:
        d[t.tag].update(('@' + k, v) for k, v in t.attrib.iteritems())
    if trim and t.text:
        t.text = t.text.strip()
    if t.text:
        if t.tag is etree.Comment and not kw.get('without_comments'):
            d['#comments'] = t.text
        elif children or t.attrib:
            d[t.tag]['#text'] = t.text
        else:
            d[t.tag] = t.text
    return d