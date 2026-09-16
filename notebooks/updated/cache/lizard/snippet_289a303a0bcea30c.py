def next(self):
    try:
        self.event, self.element = next(self.iterator)
        self.elementTag = clearTag(self.element.tag)
    except StopIteration:
        clearParsedElements(self.element)
        raise StopIteration
    return self.event, self.element, self.elementTag