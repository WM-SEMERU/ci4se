def from_array(array):
    if array is None or not array:
        return None
    assert_type_or_raise(array, dict, parameter_name='array')
    from pytgbot.api_types.sendable.reply_markup import InlineKeyboardButton
    data = {}
    data['inline_keyboard'] = InlineKeyboardButton.from_array_list(array.
        get('inline_keyboard'), list_level=2)
    instance = InlineKeyboardMarkup(**data)
    instance._raw = array
    return instance