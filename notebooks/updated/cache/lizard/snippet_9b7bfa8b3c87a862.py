def env_updated(cls, app, env):
    if cls.ABORT_AFTER_READ:
        config = {n: getattr(app.config, n) for n in (a for a in dir(app.
            config) if a.startswith('scv_'))}
        config['found_docs'] = tuple(str(d) for d in env.found_docs)
        config['master_doc'] = str(app.config.master_doc)
        cls.ABORT_AFTER_READ.put(config)
        sys.exit(0)