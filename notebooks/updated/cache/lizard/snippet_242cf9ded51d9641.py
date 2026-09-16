def parseLinkAttrs(html):
    stripped = removed_re.sub('', html)
    html_mo = html_find.search(stripped)
    if html_mo is None or html_mo.start('contents') == -1:
        return []
    start, end = html_mo.span('contents')
    head_mo = head_find.search(stripped, start, end)
    if head_mo is None or head_mo.start('contents') == -1:
        return []
    start, end = head_mo.span('contents')
    link_mos = link_find.finditer(stripped, head_mo.start(), head_mo.end())
    matches = []
    for link_mo in link_mos:
        start = link_mo.start() + 5
        link_attrs = {}
        for attr_mo in attr_find.finditer(stripped, start):
            if attr_mo.lastgroup == 'end_link':
                break
            attr_name, q_val, unq_val = attr_mo.group('attr_name', 'q_val',
                'unq_val')
            attr_val = ent_replace.sub(replaceEnt, unq_val or q_val)
            link_attrs[attr_name] = attr_val
        matches.append(link_attrs)
    return matches