def _get_text(node, tag, default=None):
    try:
        return node.find(tag).text
    except AttributeError:
        return default