def delete(self, invoice_id, **kwargs):
    url = '{}/{}'.format(self.base_url, invoice_id)
    return self.delete_url(url, {}, **kwargs)