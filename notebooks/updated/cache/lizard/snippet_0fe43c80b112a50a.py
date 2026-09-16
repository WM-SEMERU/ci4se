def get_dependency_artifacts(self, id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('callback'):
        return self.get_dependency_artifacts_with_http_info(id, **kwargs)
    else:
        data = self.get_dependency_artifacts_with_http_info(id, **kwargs)
        return data