def check_indent(self, definition, docstring):
    if docstring:
        indent = self._get_docstring_indent(definition, docstring)
        lines = docstring.split('\n')
        if len(lines) > 1:
            lines = lines[1:]
            indents = [leading_space(l) for l in lines if not is_blank(l)]
            if set(' \t') == set(''.join(indents) + indent):
                yield violations.D206()
            if len(indents) > 1 and min(indents[:-1]) > indent or indents[-1
                ] > indent:
                yield violations.D208()
            if min(indents) < indent:
                yield violations.D207()