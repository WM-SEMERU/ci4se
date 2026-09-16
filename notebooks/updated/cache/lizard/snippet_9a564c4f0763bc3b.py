def init_patcher(app, db):
    app.config.setdefault('MONGOPATCHER_PATCHES_DIR', 'patches')
    app.config.setdefault('MONGOPATCHER_COLLECTION', 'mongopatcher')
    if not hasattr(app, 'extensions'):
        app.extensions = {}
    if 'mongopatcher' not in app.extensions:
        mp = MongoPatcher(db=db, patches_dir=app.config[
            'MONGOPATCHER_PATCHES_DIR'], collection=app.config[
            'MONGOPATCHER_COLLECTION'])
        app.extensions['mongopatcher'] = mp
    else:
        raise Exception('Extension already initialized')
    if 'MONGOPATCHER_DATAMODEL_VERSION' not in app.config:
        patches = mp.discover(app.config['MONGOPATCHER_PATCHES_DIR'])
        last_version = patches[-1].target_version if patches else '1.0.0'
        app.config.setdefault('MONGOPATCHER_DATAMODEL_VERSION', last_version)
    mp.__class__.need_upgrade = need_upgrade
    mp.app_datamodel_version = app.config['MONGOPATCHER_DATAMODEL_VERSION']
    return mp