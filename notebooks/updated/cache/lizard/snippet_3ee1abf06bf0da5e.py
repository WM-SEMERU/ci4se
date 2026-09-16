def add_distributed_artifact(self, id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('callback'):
        return self.add_distributed_artifact_with_http_info(id, **kwargs)
    else:
        data = self.add_distributed_artifact_with_http_info(id, **kwargs)
        return data