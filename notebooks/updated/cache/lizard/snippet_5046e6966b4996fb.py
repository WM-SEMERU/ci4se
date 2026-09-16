def join_room(self, room_id_or_alias):
    if not room_id_or_alias:
        raise MatrixError('No alias or room ID to join.')
    path = '/join/%s' % quote(room_id_or_alias)
    return self._send('POST', path)