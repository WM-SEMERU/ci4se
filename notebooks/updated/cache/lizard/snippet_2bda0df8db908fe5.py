def render(template_path, output_file=None, **kwargs):
    template = get_template(template_path)
    rendered = template.render(**kwargs)
    if not output_file:
        return rendered
    with open(output_file) as f:
        f.write(rendered)