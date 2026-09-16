def set_chat_sticker_set(self, chat_id, sticker_set_name):
    assert_type_or_raise(chat_id, (int, unicode_type), parameter_name='chat_id'
        )
    assert_type_or_raise(sticker_set_name, unicode_type, parameter_name=
        'sticker_set_name')
    result = self.do('setChatStickerSet', chat_id=chat_id, sticker_set_name
        =sticker_set_name)
    if self.return_python_objects:
        logger.debug('Trying to parse {data}'.format(data=repr(result)))
        try:
            return from_array_list(bool, result, list_level=0, is_builtin=True)
        except TgApiParseException:
            logger.debug('Failed parsing as primitive bool', exc_info=True)
        raise TgApiParseException('Could not parse result.')
    return result