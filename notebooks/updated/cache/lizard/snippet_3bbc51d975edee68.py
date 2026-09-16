def process(self, content):
    log.debug('processing:\n%s', content)
    self.reset()
    if content.tag is None:
        content.tag = content.value.__class__.__name__
    document = Document()
    if isinstance(content.value, Property):
        root = self.node(content)
        self.append(document, content)
    else:
        self.append(document, content)
    return document.root()