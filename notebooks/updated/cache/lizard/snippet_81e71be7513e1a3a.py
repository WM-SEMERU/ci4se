def commit(cls, client=None):
    if not client:
        client = cls._client
    rtn = client.write_points(cls._json_body_())
    cls._reset_()
    return rtn