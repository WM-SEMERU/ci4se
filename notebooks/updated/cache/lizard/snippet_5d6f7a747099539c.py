def append(self, items):
    resp = self.client.add_to_item_list(items, self.url())
    self.refresh()
    return resp