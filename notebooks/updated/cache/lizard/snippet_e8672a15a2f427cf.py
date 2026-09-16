def copy_binder_files(app, exception):
    if exception is not None:
        return
    if app.builder.name not in ['html', 'readthedocs']:
        return
    gallery_conf = app.config.sphinx_gallery_conf
    binder_conf = check_binder_conf(gallery_conf.get('binder'))
    if not len(binder_conf) > 0:
        return
    logger.info('copying binder requirements...', color='white')
    _copy_binder_reqs(app, binder_conf)
    _copy_binder_notebooks(app)