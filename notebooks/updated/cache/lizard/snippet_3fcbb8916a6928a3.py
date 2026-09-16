def get_colorscheme(self, scheme_file):
    scheme = get_yaml_dict(scheme_file)
    scheme_slug = builder.slugify(scheme_file)
    builder.format_scheme(scheme, scheme_slug)
    try:
        temp_base, temp_sub = self.temp.split('##')
    except ValueError:
        temp_base, temp_sub = self.temp.strip('##'), 'default'
    temp_path = rel_to_cwd('templates', temp_base)
    temp_group = builder.TemplateGroup(temp_path)
    try:
        single_temp = temp_group.templates[temp_sub]
    except KeyError:
        raise FileNotFoundError(None, None, self.path + ' (sub-template)')
    colorscheme = pystache.render(single_temp['parsed'], scheme)
    return colorscheme