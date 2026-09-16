def render_json(tree, indent):
    return json.dumps([{'package': k.as_dict(), 'dependencies': [v.as_dict(
        ) for v in vs]} for k, vs in tree.items()], indent=indent)