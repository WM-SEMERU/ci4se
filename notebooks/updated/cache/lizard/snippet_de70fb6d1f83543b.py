def recClearTag(element):
    children = element.getchildren()
    if len(children) > 0:
        for child in children:
            recClearTag(child)
    element.tag = clearTag(element.tag)