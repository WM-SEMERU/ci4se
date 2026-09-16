def get_rendered_fields(self, ctx=None):
    if ctx is None:
        ctx = RenderContext()
    ctx.push(self)
    result = []
    for f in self._fields:
        if len(f.render(ctx)):
            result.append(f)
    ctx.pop()
    return result