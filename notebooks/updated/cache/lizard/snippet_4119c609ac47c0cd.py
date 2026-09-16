def partial_jinja_template(template_name, name='data', mimetype='text/html'):

    def partial_jinja_renderer(result, errors):
        template = get_jinja_template(template_name)
        old = template.environment.undefined
        template.environment.undefined = DebugUndefined
        context = {name: result or Mock(), 'errors': errors}
        rendered = template.render(**context)
        template.environment.undefined = old
        return {'body': rendered, 'mimetype': mimetype}
    return partial_jinja_renderer