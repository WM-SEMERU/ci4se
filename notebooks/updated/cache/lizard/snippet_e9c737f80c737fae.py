def publish(self, vhost, xname, rt_key, payload, payload_enc='string',
    properties=None):
    vhost = quote(vhost, '')
    xname = quote(xname, '')
    path = Client.urls['publish_to_exchange'] % (vhost, xname)
    body = json.dumps({'routing_key': rt_key, 'payload': payload,
        'payload_encoding': payload_enc, 'properties': properties or {}})
    result = self._call(path, 'POST', body)
    return result['routed']