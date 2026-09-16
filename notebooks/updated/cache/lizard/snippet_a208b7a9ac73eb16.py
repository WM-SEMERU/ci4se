def all(self):
    if not self.is_any and not self.is_none:
        return [Element.from_href(href) for href in self.get(self.typeof)]
    return []