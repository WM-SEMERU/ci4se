def refresh(self):
    refreshed = self.client.get_item_list(self.url())
    self.item_urls = refreshed.urls()
    self.list_name = refreshed.name()
    return self