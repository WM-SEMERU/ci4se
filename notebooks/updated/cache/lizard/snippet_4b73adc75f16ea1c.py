def make_site(cls, searchpath='templates', outpath='.', contexts=None,
    rules=None, encoding='utf8', followlinks=True, extensions=None,
    staticpaths=None, filters=None, env_globals=None, env_kwargs=None,
    mergecontexts=False):
    if not os.path.isabs(searchpath):
        calling_module = inspect.getmodule(inspect.stack()[-1][0])
        project_path = os.path.realpath(os.path.dirname(calling_module.
            __file__))
        searchpath = os.path.join(project_path, searchpath)
    if env_kwargs is None:
        env_kwargs = {}
    env_kwargs['loader'] = FileSystemLoader(searchpath=searchpath, encoding
        =encoding, followlinks=followlinks)
    env_kwargs.setdefault('extensions', extensions or [])
    environment = Environment(**env_kwargs)
    if filters:
        environment.filters.update(filters)
    if env_globals:
        environment.globals.update(env_globals)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    return cls(environment, searchpath=searchpath, outpath=outpath,
        encoding=encoding, logger=logger, rules=rules, contexts=contexts,
        staticpaths=staticpaths, mergecontexts=mergecontexts)