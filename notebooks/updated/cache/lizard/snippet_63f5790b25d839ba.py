def construct_arg(cls, name, params):
    use_snippet = params.pop('use', None)
    if use_snippet:
        try:
            problem = None
            snippet = (yaml_snippet_loader.YamlSnippetLoader.
                get_snippet_by_name(use_snippet))
            params = dict(snippet.args.pop(name), **params)
        except KeyError:
            problem = "Couldn't find arg {arg} in snippet {snip}.".format(arg
                =name, snip=snippet.name)
            raise exceptions.ExecutionException(problem)
    if 'flags' not in params:
        msg = 'Couldn\'t find "flags" in arg {arg}'.format(arg=name)
        raise exceptions.ExecutionException(msg)
    return cls(name, *params.pop('flags'), **params)