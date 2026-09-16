def delete_row(self, index):
    url = self.build_url(self._endpoints.get('delete_row').format(id=index))
    return bool(self.session.post(url))