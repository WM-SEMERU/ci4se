def next(self):
    if self.idx >= len(self.page_list):
        raise StopIteration()
    page = self.page_list[self.idx]
    self.idx += 1
    return page