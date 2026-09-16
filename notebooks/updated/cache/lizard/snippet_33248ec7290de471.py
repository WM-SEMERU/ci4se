def save_message(self):
    if self.object_id and not self.__is_draft:
        allowed_changes = {self._cc('isRead'), self._cc('categories'), self
            ._cc('flag')}
        changes = {tc for tc in self._track_changes if tc in allowed_changes}
        if not changes:
            return True
        url = self.build_url(self._endpoints.get('get_message').format(id=
            self.object_id))
        data = self.to_api_data(restrict_keys=changes)
        response = self.con.patch(url, data=data)
        if not response:
            return False
        self._track_changes.clear()
        self.__modified = self.protocol.timezone.localize(dt.datetime.now())
        return True
    else:
        return self.save_draft()