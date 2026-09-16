def glitter_startbody(context):
    user = context.get('user')
    path_body = 'glitter/include/startbody.html'
    path_plus = 'glitter/include/startbody_%s_%s.html'
    rendered = ''
    if user is not None and user.is_staff:
        templates = [path_body]
        glitter = context.get('glitter')
        if glitter is not None:
            opts = glitter.obj._meta.app_label, glitter.obj._meta.model_name
            template_path = path_plus % opts
            templates.insert(0, template_path)
        template = context.template.engine.select_template(templates)
        rendered = template.render(context)
    return rendered