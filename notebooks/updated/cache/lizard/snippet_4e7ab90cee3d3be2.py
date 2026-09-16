def render(template, context=None, **kwargs):
    renderer = Renderer()
    return renderer.render(template, context, **kwargs)