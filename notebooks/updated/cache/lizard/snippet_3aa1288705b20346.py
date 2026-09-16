def format_item(format_spec, item, defaults=None):
    template_engine = getattr(format_spec, '__engine__', None)
    if (template_engine == 'tempita' or not template_engine and format_spec
        .startswith('{{')):
        namespace = dict(headers=not bool(item))
        if item:
            namespace['d'] = item
        else:
            namespace['d'] = Bunch()
            for name in engine.FieldDefinition.FIELDS:
                namespace['d'][name] = name.upper()
            namespace.update((name[4:], lambda x, m=method: str(x).rjust(
                len(str(m(0))))) for name, method in globals().items() if
                name.startswith('fmt_'))
        return expand_template(format_spec, namespace)
    else:
        format_spec = getattr(format_spec, 'fmt', format_spec)
        if item is None:
            format_spec = re.sub(
                '(\\([_.a-zA-Z0-9]+\\)[-#+0 ]?[0-9]*?)[.0-9]*[diouxXeEfFgG]',
                lambda m: m.group(1) + 's', format_spec)
        return format_spec % OutputMapping(item, defaults)