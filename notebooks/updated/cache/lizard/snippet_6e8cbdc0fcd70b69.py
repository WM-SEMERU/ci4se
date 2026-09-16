def get_broadcasts(self, type='', page=None, remote_content_id=None, limit=
    None, **kwargs):
    if remote_content_id:
        return self.get_broadcasts_by_remote(remote_content_id)
    params = {'type': type}
    if page:
        params['page'] = page
    params.update(kwargs)
    result = self._call('broadcasts', params=params, content_type=
        'application/json')
    broadcasts = [Broadcast(b) for b in result]
    if limit:
        return broadcasts[:limit]
    return broadcasts