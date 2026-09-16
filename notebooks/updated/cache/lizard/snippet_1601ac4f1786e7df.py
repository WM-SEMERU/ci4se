def get_api_docs(routes):
    routes = map(_get_tuple_from_route, routes)
    documentation = []
    for url, rh, methods in sorted(routes, key=lambda a: a[0]):
        if issubclass(rh, APIHandler):
            documentation.append(_get_route_doc(url, rh, methods))
    documentation = (
        '**This documentation is automatically generated.**\n\n' +
        '**Output schemas only represent `data` and not the full output; ' +
        """see output examples and the JSend specification.**
""" +
        '\n<br>\n<br>\n'.join(documentation))
    return documentation