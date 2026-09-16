def _load_torrents_directory(self):
    r = self._req_lixian_get_id(torrent=True)
    self._downloads_directory = self._load_directory(r['cid'])