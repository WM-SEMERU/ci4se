def get_template(template_dict, parameter_overrides=None):
    template_dict = template_dict or {}
    if template_dict:
        template_dict = SamTranslatorWrapper(template_dict).run_plugins()
    template_dict = SamBaseProvider._resolve_parameters(template_dict,
        parameter_overrides)
    ResourceMetadataNormalizer.normalize(template_dict)
    return template_dict