def im_set_topic(self, room_id, topic, **kwargs):
    return self.__call_api_post('im.setTopic', roomId=room_id, topic=topic,
        kwargs=kwargs)