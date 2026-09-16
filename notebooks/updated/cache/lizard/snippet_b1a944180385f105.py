def _item_type(item):
    tag = item['tag']
    style = item.get('style', None)
    if tag == 'p':
        if style is None or 'paragraph' in style:
            return 'paragraph'
        else:
            return style
    elif tag == 'span':
        if style in (None, 'normal-text'):
            return 'text'
        elif style == 'url':
            return 'link'
        else:
            return style
    elif tag == 'h':
        assert style is not None
        return style
    elif tag in ('list', 'list-item', 'line-break'):
        if style == '_numbered_list':
            return 'numbered-list'
        else:
            return tag
    elif tag == 's':
        return 'spaces'
    raise Exception("The tag '{0}' with style '{1}' hasn't been implemented."
        .format(tag, style))