def render(self, sphinx_app: Sphinx, context):
    builder: StandaloneHTMLBuilder = sphinx_app.builder
    resource = sphinx_app.env.resources[self.docname]
    context['sphinx_app'] = sphinx_app
    context['widget'] = self
    context['resource'] = resource
    self.make_context(context, sphinx_app)
    template = self.template + '.html'
    html = builder.templates.render(template, context)
    return html