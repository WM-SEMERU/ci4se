def delete(self, ids):
    url = build_uri_with_ids('api/v4/as/%s/', ids)
    return super(ApiV4As, self).delete(url)