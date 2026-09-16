def html_list(data):
    if data is None:
        return None
    as_li = lambda v: '<li>%s</li>' % v
    items = [as_li(v) for v in data]
    return mark_safe('<ul>%s</ul>' % ''.join(items))