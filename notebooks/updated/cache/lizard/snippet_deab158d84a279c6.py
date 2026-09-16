def render_file(context, path, absolute=False):
    site = g.current_site
    if not absolute:
        path = os.path.join(site.path, path)
    return render_template(path, **context)