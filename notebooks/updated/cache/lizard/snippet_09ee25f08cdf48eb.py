def delete(self, id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('callback'):
        return self.delete_with_http_info(id, **kwargs)
    else:
        data = self.delete_with_http_info(id, **kwargs)
        return data