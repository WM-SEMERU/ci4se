def strong(node):
    o = nodes.strong()
    for n in MarkDown(node):
        o += n
    return o