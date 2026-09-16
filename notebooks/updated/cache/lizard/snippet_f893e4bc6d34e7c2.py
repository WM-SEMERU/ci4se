def update(self, title=None, description=None, images=None, cover=None,
    layout=None, privacy=None):
    url = self._imgur._base_url + '/3/album/{0}'.format(self._delete_or_id_hash
        )
    is_updated = self._imgur._send_request(url, params=locals(), method='POST')
    if is_updated:
        self.title = title or self.title
        self.description = description or self.description
        self.layout = layout or self.layout
        self.privacy = privacy or self.privacy
        if cover is not None:
            self.cover = cover if isinstance(cover, Image) else Image({'id':
                cover}, self._imgur, has_fetched=False)
        if images:
            self.images = [(img if isinstance(img, Image) else Image({'id':
                img}, self._imgur, False)) for img in images]
    return is_updated