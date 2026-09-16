def create_feature(self, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('callback'):
        return self.create_feature_with_http_info(**kwargs)
    else:
        data = self.create_feature_with_http_info(**kwargs)
        return data