def authenticate(cls, client_id, secret):
    result = yield views.oauth_client.get(key=[secret, client_id])
    if not result['rows']:
        raise Return()
    service = yield Service.get(client_id)
    raise Return(service)