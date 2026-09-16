def _filter(self, text, context, encoding):
    content = []
    blocks, attributes, comments = self.to_text(bs4.BeautifulSoup(text,
        self.parser))
    if self.comments:
        for c, desc in comments:
            content.append(filters.SourceText(c, context + ': ' + desc,
                encoding, self.type + 'comment'))
    if self.attributes:
        for a, desc in attributes:
            content.append(filters.SourceText(a, context + ': ' + desc,
                encoding, self.type + 'attribute'))
    for b, desc in blocks:
        content.append(filters.SourceText(b, context + ': ' + desc,
            encoding, self.type + 'content'))
    return content