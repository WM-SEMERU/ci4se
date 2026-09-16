def update_favorite_song(self, song_id, op):
    op = 'un' if op == 'del' else ''
    action = 'mtop.alimusic.fav.songfavoriteservice.{}favoritesong'.format(op)
    payload = {'songId': song_id}
    code, msg, rv = self.request(action, payload)
    return rv['data']['data']['status'] == 'true'