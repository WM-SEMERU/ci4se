def get_or_create_head(root):
    head = _create_cssselector('head')(root)
    if not head:
        head = etree.Element('head')
        body = _create_cssselector('body')(root)[0]
        body.getparent().insert(0, head)
        return head
    else:
        return head[0]