def charts_slug_get(self, slug, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('callback'):
        return self.charts_slug_get_with_http_info(slug, **kwargs)
    else:
        data = self.charts_slug_get_with_http_info(slug, **kwargs)
        return data