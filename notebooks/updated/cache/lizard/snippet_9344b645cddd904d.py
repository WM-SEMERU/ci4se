def absolute(parser, token):
    node = url(parser, token)
    return AbsoluteUrlNode(view_name=node.view_name, args=node.args, kwargs
        =node.kwargs, asvar=node.asvar)