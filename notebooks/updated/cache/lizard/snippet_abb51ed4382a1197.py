def change_settings(self, bio=None, public_images=None, messaging_enabled=
    None, album_privacy=None, accepted_gallery_terms=None):
    url = self._imgur._base_url + '/3/account/{0}/settings'.format(self.name)
    resp = self._imgur._send_request(url, needs_auth=True, params=locals(),
        method='POST')
    return resp