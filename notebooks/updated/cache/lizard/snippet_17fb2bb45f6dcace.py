def deserialize(stream_or_string, **options):
    options.setdefault('Loader', Loader)
    try:
        return yaml.load(stream_or_string, **options)
    except ScannerError as error:
        log.exception('Error encountered while deserializing')
        err_type = ERROR_MAP.get(error.problem, 'Unknown yaml render error')
        line_num = error.problem_mark.line + 1
        raise DeserializationError(err_type, line_num, error.problem_mark.
            buffer)
    except ConstructorError as error:
        log.exception('Error encountered while deserializing')
        raise DeserializationError(error)
    except Exception as error:
        log.exception('Error encountered while deserializing')
        raise DeserializationError(error)