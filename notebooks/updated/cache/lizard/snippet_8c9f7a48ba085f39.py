def set_keywords(self, keywords):
    self.head.keywords.attr(content=', '.join(keywords))
    return self