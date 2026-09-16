def markdown(text, renderer=None, **options):
    ext, rndr = make_flags(**options)
    if renderer:
        md = misaka.Markdown(renderer, ext)
        result = md(text)
    else:
        result = misaka.html(text, extensions=ext, render_flags=rndr)
    if options.get('smartypants'):
        result = misaka.smartypants(result)
    return Markup(result)