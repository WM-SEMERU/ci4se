def insert_into_last_element(html, element):
    try:
        item = fragment_fromstring(element)
    except (ParserError, TypeError) as e:
        item = fragment_fromstring('<span></span>')
    try:
        doc = fragments_fromstring(html)
        doc[-1].append(item)
        return ''.join(tostring(e) for e in doc)
    except (ParserError, TypeError) as e:
        return ''