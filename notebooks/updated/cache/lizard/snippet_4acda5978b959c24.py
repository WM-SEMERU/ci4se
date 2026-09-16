def get_page(self, paginator):
    page = int(self.get_and_save_value('page', 1))
    if page < 1:
        return self.save_value('page', 1)
    if page > paginator.num_pages:
        return self.save_value('page', paginator.num_pages)
    return page