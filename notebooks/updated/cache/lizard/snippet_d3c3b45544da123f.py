def render_toctrees(kb_app: kb, sphinx_app: Sphinx, doctree: doctree,
    fromdocname: str):
    settings: KaybeeSettings = sphinx_app.config.kaybee_settings
    if not settings.articles.use_toctree:
        return
    builder: StandaloneHTMLBuilder = sphinx_app.builder
    env: BuildEnvironment = sphinx_app.env
    registered_toctree = ToctreeAction.get_for_context(kb_app)
    for node in doctree.traverse(toctree):
        if node.attributes['hidden']:
            continue
        custom_toctree = registered_toctree(fromdocname)
        context = builder.globalcontext.copy()
        context['sphinx_app'] = sphinx_app
        entries = node.attributes['entries']
        custom_toctree.set_entries(entries, env.titles, sphinx_app.env.
            resources)
        output = custom_toctree.render(builder, context, sphinx_app)
        listing = [nodes.raw('', output, format='html')]
        node.replace_self(listing)