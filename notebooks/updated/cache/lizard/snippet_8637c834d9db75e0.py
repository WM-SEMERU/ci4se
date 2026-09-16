def default_output_format(content_type='application/json', apply_globally=
    False, api=None, cli=False, http=True):

    def decorator(formatter):
        formatter = hug.output_format.content_type(content_type)(formatter)
        if apply_globally:
            if http:
                hug.defaults.output_format = formatter
            if cli:
                hug.defaults.cli_output_format = formatter
        else:
            apply_to_api = hug.API(api) if api else hug.api.from_object(
                formatter)
            if http:
                apply_to_api.http.output_format = formatter
            if cli:
                apply_to_api.cli.output_format = formatter
        return formatter
    return decorator