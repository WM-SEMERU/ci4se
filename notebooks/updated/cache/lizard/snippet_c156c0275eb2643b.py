def jinja_template(template_name, name='data', mimetype='text/html'):

    def jinja_renderer(result, errors):
        template = get_jinja_template(template_name)
        context = {name: result or Mock(), 'errors': errors, 'enumerate':
            enumerate}
        rendered = template.render(**context)
        return {'body': rendered, 'mimetype': mimetype}
    return jinja_renderer