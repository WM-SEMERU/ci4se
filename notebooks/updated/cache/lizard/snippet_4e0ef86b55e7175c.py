def html(self, text=TEXT):
    self.logger.debug('Generating the HTML report{}...'.format(['',
        ' (text only)'][text]))
    html = []
    for piece in self._pieces:
        if isinstance(piece, string_types):
            html.append(markdown2.markdown(piece, extras=['tables']))
        elif isinstance(piece, Element):
            html.append(piece.html())
    return '\n\n'.join(html)