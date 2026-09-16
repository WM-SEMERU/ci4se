def _delete_map_from_user_by_id(self, user, map_id):
    map = self._get_map_from_user_by_id(user, map_id)
    if map is None:
        return None
    Session.delete(map)
    Session.commit()
    return map