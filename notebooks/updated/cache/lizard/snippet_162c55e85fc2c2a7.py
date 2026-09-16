def to_html(self, codebase):
    body = ''
    for section in ('params', 'options', 'exceptions'):
        val = getattr(self, section)
        if val:
            body += '<h5>%s</h5>\n<dl class = "%s">%s</dl>' % (printable(
                section), section, '\n'.join(param.to_html() for param in val))
    body += codebase.build_see_html(self.see, 'h5', self)
    return ('<a name = "%s" />\n<div class = "function">\n' +
        '<h4>%s</h4>\n%s\n%s\n</div>\n') % (self.name, self.name,
        htmlize_paragraphs(codebase.translate_links(self.doc, self)), body)