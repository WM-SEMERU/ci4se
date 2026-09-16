def category(self, category):
    self.url.category = category
    self.url.set_page(1)
    return self