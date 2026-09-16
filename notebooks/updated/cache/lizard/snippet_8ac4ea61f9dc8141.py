def render(dson_input, saltenv='base', sls='', **kwargs):
    if not isinstance(dson_input, six.string_types):
        dson_input = dson_input.read()
    log.debug('DSON input = %s', dson_input)
    if dson_input.startswith('#!'):
        dson_input = dson_input[dson_input.find('\n') + 1:]
    if not dson_input.strip():
        return {}
    return dson.loads(dson_input)