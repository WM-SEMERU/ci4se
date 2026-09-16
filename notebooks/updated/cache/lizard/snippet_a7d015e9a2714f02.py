def get_template(template_name, using=None):
    engines = _engine_list(using)
    for engine in engines:
        try:
            return engine.get_template(template_name)
        except TemplateDoesNotExist as e:
            pass
    raise TemplateDoesNotExist(template_name)