def _presence_listener(self, event: Dict[str, Any]):
    if self._stop_event.ready():
        return
    user_id = event['sender']
    if event['type'] != 'm.presence' or user_id == self._user_id:
        return
    user = self._get_user(user_id)
    user.displayname = event['content'].get('displayname') or user.displayname
    address = self._validate_userid_signature(user)
    if not address:
        return
    if not self.is_address_known(address):
        return
    self.add_userid_for_address(address, user_id)
    new_state = UserPresence(event['content']['presence'])
    if new_state == self._userid_to_presence.get(user_id):
        return
    self._userid_to_presence[user_id] = new_state
    self.refresh_address_presence(address)
    if self._user_presence_changed_callback:
        self._user_presence_changed_callback(user, new_state)