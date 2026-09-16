def channels_unarchive(self, room_id, **kwargs):
    return self.__call_api_post('channels.unarchive', roomId=room_id,
        kwargs=kwargs)