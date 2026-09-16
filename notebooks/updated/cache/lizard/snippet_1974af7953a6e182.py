def _render_before(self, element):
    start = ['%s<%s' % (self.spaces, element.tag)]
    if element.id:
        start.append(' id=%s' % self.element.attr_wrap(self.
            replace_inline_variables(element.id)))
    if element.classes:
        start.append(' class=%s' % self.element.attr_wrap(self.
            replace_inline_variables(element.classes)))
    if element.attributes:
        start.append(' ' + self.replace_inline_variables(element.attributes))
    content = self._render_inline_content(self.element.inline_content)
    if element.nuke_inner_whitespace and content:
        content = content.strip()
    if element.self_close and not content:
        start.append(' />')
    elif content:
        start.append('>%s' % content)
    elif self.children:
        start.append('>%s' % self.render_newlines())
    else:
        start.append('>')
    return ''.join(start)