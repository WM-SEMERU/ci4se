def renders_impl(self, template_content, context, at_paths=None,
    at_encoding=anytemplate.compat.ENCODING, **kwargs):
    renderer = self._make_renderer(at_paths, at_encoding, **kwargs)
    ctxs = [] if context is None else [context]
    return renderer.render(template_content, *ctxs)