def prettify(self, depth=0, separator='  ', last=True, pre=False, inline=False
    ):
    output = ''
    if self.getTagName() != '' and self.tagToString().strip() == '':
        return ''
    if not pre and not inline:
        output += depth * separator
    if self.getTagName().lower() == 'pre' and self.isOpeningTag():
        pre = True
        separator = ''
    output += self.tagToString()
    is_inline = inline
    for c in self.childs:
        if not (c.isTag() or c.isComment()):
            if len(c.tagToString().strip()) != 0:
                inline = True
    original_depth = depth
    if self.getTagName() != '':
        if not pre and not inline:
            depth += 1
            if self.tagToString().strip() != '':
                output += '\n'
    for e in self.childs:
        if not e.isEndTag():
            output += e.prettify(depth, last=False, pre=pre, inline=inline)
    if self.endtag is not None:
        if not pre and not inline:
            output += original_depth * separator
        output += self.endtag.tagToString().strip()
        if not is_inline:
            output += '\n'
    return output