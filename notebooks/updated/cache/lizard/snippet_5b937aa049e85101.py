def dict(self):
    collection = dict(page=self.page, per_page=self.per_page, total_items=
        self.total_items, total_pages=self.total_pages, pagination=self.
        pagination, items=list(self.items))
    return collection