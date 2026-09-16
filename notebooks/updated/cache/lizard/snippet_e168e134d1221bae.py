def datasets_download(self, owner_slug, dataset_slug, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.datasets_download_with_http_info(owner_slug,
            dataset_slug, **kwargs)
    else:
        data = self.datasets_download_with_http_info(owner_slug,
            dataset_slug, **kwargs)
        return data