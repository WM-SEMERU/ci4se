def start_health_check(self, node_address):
    if self._stop_event.ready():
        return
    with self._health_lock:
        if self._address_mgr.is_address_known(node_address):
            return
        node_address_hex = to_normalized_address(node_address)
        self.log.debug('Healthcheck', peer_address=node_address_hex)
        candidates = [self._get_user(user) for user in self._client.
            search_user_directory(node_address_hex)]
        user_ids = {user.user_id for user in candidates if 
            validate_userid_signature(user) == node_address}
        self.whitelist(node_address)
        self._address_mgr.add_userids_for_address(node_address, user_ids)
        self._address_mgr.refresh_address_presence(node_address)