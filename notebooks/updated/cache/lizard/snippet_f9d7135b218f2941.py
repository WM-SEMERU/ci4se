def _set_color(self, context, r, g, b, a):
    if a < 1:
        context.set_source_rgba(r, g, b, a)
    else:
        context.set_source_rgb(r, g, b)