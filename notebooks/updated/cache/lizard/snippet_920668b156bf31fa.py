def cli_certify_core_integer(config, min_value, max_value, value):

    def parser(v):
        try:
            v = load_json_pickle(v, config)
        except Exception:
            pass
        try:
            return int(v)
        except Exception as err:
            six.raise_from(CertifierTypeError(message='Not integer: {x}'.
                format(x=v), value=v), err)
    execute_cli_command('integer', config, parser, certify_int, value[0] if
        value else None, min_value=min_value, max_value=max_value, required
        =config['required'])