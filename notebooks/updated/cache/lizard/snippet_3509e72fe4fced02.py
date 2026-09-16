def create_binding(self, vhost, exchange, queue, rt_key=None, args=None):
    vhost = quote(vhost, '')
    exchange = quote(exchange, '')
    queue = quote(queue, '')
    body = json.dumps({'routing_key': rt_key, 'arguments': args or []})
    path = Client.urls['bindings_between_exch_queue'] % (vhost, exchange, queue
        )
    binding = self._call(path, 'POST', body=body, headers=Client.json_headers)
    return binding