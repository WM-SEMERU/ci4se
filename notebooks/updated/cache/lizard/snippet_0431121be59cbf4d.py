def extract(self, obj, bypass_ref=False):
    try:
        if isinstance(obj, Mapping):
            if not bypass_ref and '$ref' in obj:
                raise RefError(obj, 'presence of a $ref member')
            obj = self.extract_mapping(obj)
        elif isinstance(obj, Sequence) and not isinstance(obj, string_types):
            obj = self.extract_sequence(obj)
        else:
            raise WrongType(obj, '{!r} does not apply for {!r}'.format(str(
                self), obj))
        if isinstance(obj, Mapping):
            if not bypass_ref and '$ref' in obj:
                raise RefError(obj, 'presence of a $ref member')
        return obj
    except ExtractError as error:
        logger.exception(error)
        raise
    except Exception as error:
        logger.exception(error)
        args = [arg for arg in error.args if arg not in (self, obj)]
        raise ExtractError(obj, *args)