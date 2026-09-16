def add_query_parameters_to_url(url, query_parameters):
    url_parts = urllib.parse.urlparse(url)
    qs_args = urllib.parse.parse_qs(url_parts[4])
    qs_args.update(query_parameters)
    sorted_qs_args = OrderedDict()
    for k in sorted(qs_args.keys()):
        sorted_qs_args[k] = qs_args[k]
    new_qs = urllib.parse.urlencode(sorted_qs_args, True)
    return urllib.parse.urlunparse(list(url_parts[0:4]) + [new_qs] + list(
        url_parts[5:]))