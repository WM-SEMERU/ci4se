def generate_context(context_file='cookiecutter.json', default_context=None,
    extra_context=None):
    context = OrderedDict([])
    try:
        with open(context_file) as file_handle:
            obj = json.load(file_handle, object_pairs_hook=OrderedDict)
    except ValueError as e:
        full_fpath = os.path.abspath(context_file)
        json_exc_message = str(e)
        our_exc_message = (
            'JSON decoding error while loading "{0}".  Decoding error details: "{1}"'
            .format(full_fpath, json_exc_message))
        raise ContextDecodingException(our_exc_message)
    file_name = os.path.split(context_file)[1]
    file_stem = file_name.split('.')[0]
    context[file_stem] = obj
    if default_context:
        apply_overwrites_to_context(obj, default_context)
    if extra_context:
        apply_overwrites_to_context(obj, extra_context)
    logger.debug('Context generated is {}'.format(context))
    return context