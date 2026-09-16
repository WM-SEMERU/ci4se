def set_avatar(self, asset_id):
    if self.get_avatar_metadata().is_read_only():
        raise errors.NoAccess()
    if not self._is_valid_id(asset_id):
        raise errors.InvalidArgument()
    self._my_map['avatarId'] = str(asset_id)