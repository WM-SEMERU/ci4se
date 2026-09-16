def set_min_priority(self, infohash_list):
    data = self._process_infohash_list(infohash_list)
    return self._post('command/bottomPrio', data=data)