def render(template: typing.Union[str, Template], **kwargs):
    if not hasattr(template, 'render'):
        template = get_environment().from_string(textwrap.dedent(template))
    return template.render(cauldron_template_uid=make_template_uid(), **kwargs)