def toc_html(self):
    if self._toc is None:
        return None

    def indent():
        return '  ' * (len(h_stack) - 1)
    lines = []
    h_stack = [0]
    for level, id, name in self._toc:
        if level > h_stack[-1]:
            lines.append('%s<ul>' % indent())
            h_stack.append(level)
        elif level == h_stack[-1]:
            lines[-1] += '</li>'
        else:
            while level < h_stack[-1]:
                h_stack.pop()
                if not lines[-1].endswith('</li>'):
                    lines[-1] += '</li>'
                lines.append('%s</ul></li>' % indent())
        lines.append('%s<li><a href="#%s">%s</a>' % (indent(), id, name))
    while len(h_stack) > 1:
        h_stack.pop()
        if not lines[-1].endswith('</li>'):
            lines[-1] += '</li>'
        lines.append('%s</ul>' % indent())
    return '\n'.join(lines) + '\n'