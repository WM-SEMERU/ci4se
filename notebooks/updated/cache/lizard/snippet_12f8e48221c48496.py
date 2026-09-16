def __get_indent(self, mimetype):
    indent = max(int(mimetype.params.get('indent', '0')), 0)
    if indent == 0:
        return None
    return indent