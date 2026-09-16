def delete_search_index(self, index):
    if not self.yz_wm_index:
        raise NotImplementedError(
            'Search 2.0 administration is not supported for this version')
    url = self.search_index_path(index)
    status, _, _ = self._request('DELETE', url)
    if status != 204:
        raise RiakError('Error setting Search 2.0 index.')
    return True