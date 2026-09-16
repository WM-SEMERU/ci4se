def broadcast_url(self, broadcast_id=None, stop=False, layout=False):
    url = self.api_url + '/v2/project/' + self.api_key + '/broadcast'
    if broadcast_id:
        url = url + '/' + broadcast_id
    if stop:
        url = url + '/stop'
    if layout:
        url = url + '/layout'
    return url