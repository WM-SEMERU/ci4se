def find_referenced_templates(template, search_path):
    from jinja2 import Environment, meta
    env = Environment()
    ast = env.parse(template.read())
    referenced_templates = list(meta.find_referenced_templates(ast))

    def realpath(tpl):
        for path in search_path:
            t = os.path.realpath(os.path.join(path, tpl))
            if os.path.isfile(t):
                return t
        return None
    return [realpath(t) for t in referenced_templates if t is not None]