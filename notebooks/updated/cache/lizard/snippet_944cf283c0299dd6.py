def get_template_i18n(template_name, locale):
    if locale is None:
        return [template_name]
    template_list = []
    parts = template_name.rsplit('.', 1)
    root = parts[0]
    suffix = parts[1]
    if locale.territory is not None:
        locale_string = '_'.join([locale.language, locale.territory])
        localized_template_path = '.'.join([root, locale_string, suffix])
        template_list.append(localized_template_path)
    localized_template_path = '.'.join([root, locale.language, suffix])
    template_list.append(localized_template_path)
    template_list.append(template_name)
    return template_list