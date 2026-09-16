def deprecated(context):
    env = context.get('env', None)
    get_info, set_info, unset_info = context.keys_of_type_exist(('envGet',
        dict), ('envSet', dict), ('envUnset', list))
    found_at_least_one = (get_info.key_in_context or set_info.
        key_in_context or unset_info.key_in_context)
    if found_at_least_one:
        env = context['env'] = {}
    else:
        return
    if get_info.key_in_context and get_info.is_expected_type:
        env['get'] = context[get_info.key]
    if set_info.key_in_context and set_info.is_expected_type:
        env['set'] = context[set_info.key]
    if unset_info.key_in_context and unset_info.is_expected_type:
        env['unset'] = context[unset_info.key]
    logger.warning(
        "envGet, envSet and envUnset are deprecated. They will stop working upon the next major release. Use the new context key env instead. It's a lot better, promise! For the moment pypyr is creating the new env key for you under the hood."
        )