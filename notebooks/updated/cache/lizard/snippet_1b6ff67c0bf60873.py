def __load_yml(self, stream):
    try:
        return yaml.load(stream, Loader=yaml.SafeLoader)
    except ValueError as e:
        cause = 'invalid yml format. %s' % str(e)
        raise InvalidFormatError(cause=cause)