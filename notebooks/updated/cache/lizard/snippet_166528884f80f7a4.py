def contains_raw(self, etag):
    etag, weak = unquote_etag(etag)
    if weak:
        return self.contains_weak(etag)
    return self.contains(etag)