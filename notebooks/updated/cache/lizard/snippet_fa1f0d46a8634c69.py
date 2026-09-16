def addQuickElement(self, name, contents=None, attrs=None, escape=True,
    cdata=False):
    if attrs is None:
        attrs = {}
    self.startElement(name, attrs)
    if contents is not None:
        self.characters(contents, escape=escape, cdata=cdata)
    self.endElement(name)