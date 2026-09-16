def category(self):
    if self.api and self.category_id:
        return self.api._get_category(self.category_id)