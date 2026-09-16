def context_exclude(zap_helper, name, pattern):
    console.info('Excluding regex {0} from context with name: {1}'.format(
        pattern, name))
    with zap_error_handler():
        result = zap_helper.zap.context.exclude_from_context(contextname=
            name, regex=pattern)
        if result != 'OK':
            raise ZAPError('Excluding regex from context failed: {}'.format
                (result))