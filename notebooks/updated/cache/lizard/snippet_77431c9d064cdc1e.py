def fallback_render(template, context, at_paths=None, at_encoding=
    anytemplate.compat.ENCODING, **kwargs):
    tmpl = anytemplate.utils.find_template_from_path(template, at_paths)
    if tmpl is None:
        raise TemplateNotFound('template: %s' % template)
    try:
        return anytemplate.compat.copen(tmpl, encoding=at_encoding).read()
    except UnicodeDecodeError:
        return open(tmpl).read()