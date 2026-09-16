def send_media_group(self, chat_id, media, disable_notification=None,
    reply_to_message_id=None):
    assert_type_or_raise(chat_id, (int, unicode_type), parameter_name='chat_id'
        )
    from .api_types.sendable.input_media import InputMediaPhoto, InputMediaVideo
    files = {}
    new_media = []
    assert_type_or_raise(media, list, parameter_name='media')
    for i, medium in enumerate(media):
        assert_type_or_raise(medium, InputMediaPhoto, InputMediaVideo,
            parameter_name='media[{i}]'.format(i=i))
        assert isinstance(medium, (InputMediaPhoto, InputMediaVideo))
        new_medium, file = medium.get_request_data('pytgbot{i}'.format(i=i),
            full_data=True)
        logger.debug('InputMedia {} found.'.format(new_medium))
        new_media.append(new_medium)
        if file:
            files.update(file)
    new_media = json.dumps(new_media)
    assert_type_or_raise(disable_notification, None, bool, parameter_name=
        'disable_notification')
    assert_type_or_raise(reply_to_message_id, None, int, parameter_name=
        'reply_to_message_id')
    result = self.do('sendMediaGroup', chat_id=chat_id, media=new_media,
        files=files, disable_notification=disable_notification,
        reply_to_message_id=reply_to_message_id)
    if self.return_python_objects:
        logger.debug('Trying to parse {data}'.format(data=repr(result)))
        if not isinstance(result, list):
            raise TgApiParseException('Could not parse result als list.')
        from .api_types.receivable.updates import Message
        return [Message.from_array(msg) for msg in result]
        raise TgApiParseException('Could not parse result.')
    return result