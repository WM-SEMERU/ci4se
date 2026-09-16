def send_photo(self, chat_id, photo, caption=None, parse_mode=None,
    disable_notification=None, reply_to_message_id=None, reply_markup=None):
    from pytgbot.api_types.sendable.files import InputFile
    from pytgbot.api_types.sendable.reply_markup import ForceReply
    from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
    from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
    from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
    assert_type_or_raise(chat_id, (int, unicode_type), parameter_name='chat_id'
        )
    assert_type_or_raise(photo, (InputFile, unicode_type), parameter_name=
        'photo')
    assert_type_or_raise(caption, None, unicode_type, parameter_name='caption')
    assert_type_or_raise(parse_mode, None, unicode_type, parameter_name=
        'parse_mode')
    assert_type_or_raise(disable_notification, None, bool, parameter_name=
        'disable_notification')
    assert_type_or_raise(reply_to_message_id, None, int, parameter_name=
        'reply_to_message_id')
    assert_type_or_raise(reply_markup, None, (InlineKeyboardMarkup,
        ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply),
        parameter_name='reply_markup')
    result = self.do('sendPhoto', chat_id=chat_id, photo=photo, caption=
        caption, parse_mode=parse_mode, disable_notification=
        disable_notification, reply_to_message_id=reply_to_message_id,
        reply_markup=reply_markup)
    if self.return_python_objects:
        logger.debug('Trying to parse {data}'.format(data=repr(result)))
        from pytgbot.api_types.receivable.updates import Message
        try:
            return Message.from_array(result)
        except TgApiParseException:
            logger.debug('Failed parsing as api_type Message', exc_info=True)
        raise TgApiParseException('Could not parse result.')
    return result