def remove_tag(self, tag):
    if isinstance(tag, Tag):
        tag = tag.get_name()
    params = self._get_params()
    params['tag'] = tag
    self._request(self.ws_prefix + '.removeTag', False, params)