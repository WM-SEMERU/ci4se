def get_option(option, default=None, cast=None):
    from acorn.config import settings
    config = settings('acorn')
    if config.has_section('database') and config.has_option('database', option
        ):
        result = config.get('database', option)
        if cast is not None:
            result = cast(result)
    else:
        result = default
    return result