def prev(self, error_out=False):
    return self.query.paginate(self.page - 1, self.per_page, error_out)