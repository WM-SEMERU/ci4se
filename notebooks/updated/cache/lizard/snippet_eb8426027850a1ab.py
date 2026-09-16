def set_game_score(self, user_id, score, force=False, disable_edit_message=
    False, chat_id=None, message_id=None, inline_message_id=None):
    assert_type_or_raise(user_id, int, parameter_name='user_id')
    assert_type_or_raise(score, int, parameter_name='score')
    assert_type_or_raise(force, None, bool, parameter_name='force')
    assert_type_or_raise(disable_edit_message, None, bool, parameter_name=
        'disable_edit_message')
    assert_type_or_raise(chat_id, None, int, parameter_name='chat_id')
    assert_type_or_raise(message_id, None, int, parameter_name='message_id')
    assert_type_or_raise(inline_message_id, None, unicode_type,
        parameter_name='inline_message_id')
    result = self.do('setGameScore', user_id=user_id, score=score, force=
        force, disable_edit_message=disable_edit_message, chat_id=chat_id,
        message_id=message_id, inline_message_id=inline_message_id)
    if self.return_python_objects:
        logger.debug('Trying to parse {data}'.format(data=repr(result)))
        from pytgbot.api_types.receivable.updates import Message
        try:
            return Message.from_array(result)
        except TgApiParseException:
            logger.debug('Failed parsing as api_type Message', exc_info=True)
        try:
            return from_array_list(bool, result, list_level=0, is_builtin=True)
        except TgApiParseException:
            logger.debug('Failed parsing as primitive bool', exc_info=True)
        raise TgApiParseException('Could not parse result.')
    return result