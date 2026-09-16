def search(self, **kwargs):
    return super(ApiVipRequest, self).get(self.prepare_url(
        'api/v3/vip-request/', kwargs))