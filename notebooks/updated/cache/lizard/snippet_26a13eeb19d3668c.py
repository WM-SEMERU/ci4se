def channels_leave(self, room_id, **kwargs):
    return self.__call_api_post('channels.leave', roomId=room_id, kwargs=kwargs
        )