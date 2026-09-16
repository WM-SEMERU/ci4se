def get_room_id(self, room_name, **kwargs):
    return GetRoomId(settings=self.settings, **kwargs).call(room_name=
        room_name, **kwargs)