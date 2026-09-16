def get_blacklist_entry(self, blacklist_entry_id):
    get_blacklist_entries_endpoint = Template(
        '${rest_root}/blacklist/${public_key}/${blacklist_entry_id}')
    url = get_blacklist_entries_endpoint.substitute(rest_root=self.
        _rest_root, public_key=self._public_key, blacklist_entry_id=
        blacklist_entry_id)
    response = self.__get_request(url)
    return response['entry']