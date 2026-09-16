def set_metadata(self, container, metadata, clear=False, prefix=None):
    if prefix is None:
        prefix = CONTAINER_META_PREFIX
    massaged = _massage_metakeys(metadata, prefix)
    new_meta = {}
    if clear:
        curr_meta = self.api.get_container_metadata(container, prefix=prefix)
        for ckey in curr_meta:
            new_meta[ckey] = ''
    utils.case_insensitive_update(new_meta, massaged)
    name = utils.get_name(container)
    uri = '/%s' % name
    resp, resp_body = self.api.method_post(uri, headers=new_meta)
    return 200 <= resp.status_code <= 299