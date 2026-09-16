def get_lyric_by_songid(self, mid):
    url = uri + '/song/lyric?' + 'id=' + str(mid) + '&lv=1&kv=1&tv=-1'
    return self.request('GET', url)