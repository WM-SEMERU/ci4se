def list_by_ids(self, ids):
    ids = utils.coerce_to_list(ids)
    uri = '/%s?ids=%s' % (self.uri_base, ','.join(ids))
    curr_prkey = self.plural_response_key
    self.plural_response_key = ''
    ret = self._list(uri)
    self.plural_response_key = curr_prkey
    return ret