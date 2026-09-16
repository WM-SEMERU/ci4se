def get_usertag(email, *tags):
    reply = _soap_client_call('get_usertag', email, *tags)
    map_el = reply('s-gensym3')
    mapping = {}
    type_attr = map_el.attributes().get('xsi:type')
    if type_attr and type_attr.value == 'apachens:Map':
        for usertag_el in (map_el.children() or []):
            tag = _uc(str(usertag_el('key')))
            buglist_el = usertag_el('value')
            mapping[tag] = [int(bug) for bug in buglist_el.children() or []]
    else:
        for usertag_el in (map_el.children() or []):
            tag = _uc(usertag_el.get_name())
            mapping[tag] = [int(bug) for bug in usertag_el.children() or []]
    return mapping