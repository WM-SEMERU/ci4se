def delete_account_metadata(self, prefix=None):
    if prefix is None:
        prefix = ACCOUNT_META_PREFIX
    curr_meta = self.get_account_metadata(prefix=prefix)
    for ckey in curr_meta:
        curr_meta[ckey] = ''
    new_meta = _massage_metakeys(curr_meta, prefix)
    uri = '/'
    resp, resp_body = self.api.method_post(uri, headers=new_meta)
    return 200 <= resp.status_code <= 299