def set_images(self, images):
    url = self._imgur._base_url + '/3/album/{0}/'.format(self.
        _delete_or_id_hash)
    params = {'ids': images}
    return self._imgur._send_request(url, needs_auth=True, params=params,
        method='POST')