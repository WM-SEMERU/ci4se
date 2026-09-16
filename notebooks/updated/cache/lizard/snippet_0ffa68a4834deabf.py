def search_order(self, limit=100, offset=0, common_name_pattern=None,
    status=None, contact_handle=None):
    response = self.request(E.searchOrderSslCertRequest(E.limit(limit), E.
        offset(offset), OE('commonNamePattern', common_name_pattern), OE(
        'status', status, transform=_simple_array), OE('contactHandle',
        contact_handle)))
    return response.as_models(SSLOrder)