def from_array(array):
    if array is None or not array:
        return None
    assert_type_or_raise(array, dict, parameter_name='array')
    from pytgbot.api_types.receivable.updates import CallbackGame
    data = {}
    data['text'] = u(array.get('text'))
    data['url'] = u(array.get('url')) if array.get('url') is not None else None
    data['callback_data'] = u(array.get('callback_data')) if array.get(
        'callback_data') is not None else None
    data['switch_inline_query'] = u(array.get('switch_inline_query')
        ) if array.get('switch_inline_query') is not None else None
    data['switch_inline_query_current_chat'] = u(array.get(
        'switch_inline_query_current_chat')) if array.get(
        'switch_inline_query_current_chat') is not None else None
    data['callback_game'] = CallbackGame.from_array(array.get('callback_game')
        ) if array.get('callback_game') is not None else None
    data['pay'] = bool(array.get('pay')) if array.get('pay'
        ) is not None else None
    instance = InlineKeyboardButton(**data)
    instance._raw = array
    return instance