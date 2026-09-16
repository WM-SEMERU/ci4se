def get_postadres_by_huisnummer(self, huisnummer):
    try:
        id = huisnummer.id
    except AttributeError:
        id = huisnummer

    def creator():
        res = crab_gateway_request(self.client,
            'GetPostadresByHuisnummerId', id)
        if res == None:
            raise GatewayResourceNotFoundException()
        return res.Postadres
    if self.caches['short'].is_configured:
        key = 'GetPostadresByHuisnummerId#%s' % id
        postadres = self.caches['short'].get_or_create(key, creator)
    else:
        postadres = creator()
    return postadres