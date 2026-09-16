def set_account_metadata(self, metadata, clear=False, prefix=None):
    if prefix is None:
        prefix = ACCOUNT_META_PREFIX
    massaged = _massage_metakeys(metadata, prefix)
    new_meta = {}
    if clear:
        curr_meta = self.get_account_metadata(prefix=prefix)
        for ckey in curr_meta:
            new_meta[ckey] = ''
        new_meta = _massage_metakeys(new_meta, prefix)
    utils.case_insensitive_update(new_meta, massaged)
    uri = '/'
    resp, resp_body = self.api.method_post(uri, headers=new_meta)
    return 200 <= resp.status_code <= 299