def strip_el_text(el, max_depth=0, cur_depth=0):
    el_text = strip_str(el.text if el.text is not None else '')
    if cur_depth < max_depth:
        for child in el:
            el_text += ' ' + strip_el_text(child, max_depth=max_depth,
                cur_depth=cur_depth + 1)
    else:
        children = list(el)
        if children is not None and len(children) > 0:
            if children[-1].tail is not None:
                el_text += ' ' + strip_str(children[-1].tail)
    if cur_depth > 0:
        if el.tail is not None:
            el_text += ' ' + strip_str(el.tail)
    return strip_str(el_text)