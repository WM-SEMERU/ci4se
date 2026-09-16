def render_without_request(template_name, template_path=None, **template_vars):
    if template_path:
        env = Environment(loader=FileSystemLoader([os.path.join(
            template_path)]))
    else:
        env = ENV
    template = env.get_template(template_name)
    return template.render(**template_vars)