def extract_args_for_httpie_main(context, method=None):
    args = _extract_httpie_options(context)
    if method:
        args.append(method.upper())
    args.append(context.url)
    args += _extract_httpie_request_items(context)
    return args