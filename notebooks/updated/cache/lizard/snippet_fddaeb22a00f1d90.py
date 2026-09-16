def remove(self, ids, **kwargs):
    url = build_uri_with_ids('api/v3/interface/%s/', ids)
    return super(ApiInterfaceRequest, self).delete(self.prepare_url(url,
        kwargs))