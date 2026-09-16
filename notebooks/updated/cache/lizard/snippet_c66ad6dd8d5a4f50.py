def op_music_to_playlist(self, mid, pid, op):
    url_add = uri + '/playlist/manipulate/tracks'
    trackIds = '["' + str(mid) + '"]'
    data_add = {'tracks': str(mid), 'pid': str(pid), 'trackIds': trackIds,
        'op': op}
    data = self.request('POST', url_add, data_add)
    code = data.get('code')
    if code == 200:
        return 1
    elif code == 502:
        return -1
    else:
        return 0