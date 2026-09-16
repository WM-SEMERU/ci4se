def answer_shipping_query(self, shipping_query_id, ok, shipping_options=
    None, error_message=None):
    from pytgbot.api_types.sendable.payments import ShippingOption
    assert_type_or_raise(shipping_query_id, unicode_type, parameter_name=
        'shipping_query_id')
    assert_type_or_raise(ok, bool, parameter_name='ok')
    assert_type_or_raise(shipping_options, None, list, parameter_name=
        'shipping_options')
    assert_type_or_raise(error_message, None, unicode_type, parameter_name=
        'error_message')
    result = self.do('answerShippingQuery', shipping_query_id=
        shipping_query_id, ok=ok, shipping_options=shipping_options,
        error_message=error_message)
    if self.return_python_objects:
        logger.debug('Trying to parse {data}'.format(data=repr(result)))
        try:
            return from_array_list(bool, result, list_level=0, is_builtin=True)
        except TgApiParseException:
            logger.debug('Failed parsing as primitive bool', exc_info=True)
        raise TgApiParseException('Could not parse result.')
    return result