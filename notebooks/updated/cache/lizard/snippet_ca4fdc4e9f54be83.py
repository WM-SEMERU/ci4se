def to_html(self, codebase):
    return ('<a name = "%s" />\n<div class = "jsclass">\n' +
        """<h3>%s</h3>
%s
<h4>Methods</h4>
%s</div>""") % (self.name, self.
        name, htmlize_paragraphs(codebase.translate_links(self.doc, self)) +
        codebase.build_see_html(self.see, 'h4', self), '\n'.join(method.
        to_html(codebase) for method in self.methods if codebase.
        include_private or not method.is_private))