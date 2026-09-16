def answer_pre_checkout_query(self, pre_checkout_query_id, ok,
    error_message=None):
    assert_type_or_raise(pre_checkout_query_id, unicode_type,
        parameter_name='pre_checkout_query_id')
    assert_type_or_raise(ok, bool, parameter_name='ok')
    assert_type_or_raise(error_message, None, unicode_type, parameter_name=
        'error_message')
    result = self.do('answerPreCheckoutQuery', pre_checkout_query_id=
        pre_checkout_query_id, ok=ok, error_message=error_message)
    if self.return_python_objects:
        logger.debug('Trying to parse {data}'.format(data=repr(result)))
        try:
            return from_array_list(bool, result, list_level=0, is_builtin=True)
        except TgApiParseException:
            logger.debug('Failed parsing as primitive bool', exc_info=True)
        raise TgApiParseException('Could not parse result.')
    return result