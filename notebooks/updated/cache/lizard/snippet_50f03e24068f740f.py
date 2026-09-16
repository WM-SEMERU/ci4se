def theme_static_with_version(ctx, filename, external=False):
    if current_app.theme_manager.static_folder:
        url = assets.cdn_for('_themes.static', filename=current.identifier +
            '/' + filename, _external=external)
    else:
        url = assets.cdn_for('_themes.static', themeid=current.identifier,
            filename=filename, _external=external)
    if url.endswith('/'):
        return url
    if current_app.config['DEBUG']:
        burst = time()
    else:
        burst = current.entrypoint.dist.version
    return '{url}?_={burst}'.format(url=url, burst=burst)