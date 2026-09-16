def get_queues(self, vhost=None):
    if vhost:
        vhost = quote(vhost, '')
        path = Client.urls['queues_by_vhost'] % vhost
    else:
        path = Client.urls['all_queues']
    queues = self._call(path, 'GET')
    return queues or list()