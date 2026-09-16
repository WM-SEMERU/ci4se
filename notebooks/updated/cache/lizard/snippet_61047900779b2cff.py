def groups_kick(self, room_id, user_id, **kwargs):
    return self.__call_api_post('groups.kick', roomId=room_id, userId=
        user_id, kwargs=kwargs)