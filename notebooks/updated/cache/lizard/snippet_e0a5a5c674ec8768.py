def select(self, limit=0):
    if limit < 1:
        limit = None
    for child in self.get_descendants(self.tag):
        if self.match(child):
            yield child
            if limit is not None:
                limit -= 1
                if limit < 1:
                    break