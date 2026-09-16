def get_templates(model):
    for template_name, template in templates.items():
        if issubclass(template.model, model):
            yield template_name, template.layout._meta.verbose_name