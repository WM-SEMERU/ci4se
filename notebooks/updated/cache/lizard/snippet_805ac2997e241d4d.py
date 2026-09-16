def get_torrent_upload_limit(self, infohash_list):
    data = self._process_infohash_list(infohash_list)
    return self._post('command/getTorrentsUpLimit', data=data)