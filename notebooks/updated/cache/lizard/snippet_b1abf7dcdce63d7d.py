def _load(formula):
    _mk_client()
    paths = []
    for ext in ('yaml', 'json'):
        source_url = salt.utils.url.create(formula + '/defaults.' + ext)
        paths.append(source_url)
    defaults_files = __context__['cp.fileclient'].cache_files(paths)
    for file_ in defaults_files:
        if not file_:
            continue
        suffix = file_.rsplit('.', 1)[-1]
        if suffix == 'yaml':
            loader = salt.utils.yaml.safe_load
        elif suffix == 'json':
            loader = salt.utils.json.load
        else:
            log.debug('Failed to determine loader for %r', file_)
            continue
        if os.path.exists(file_):
            log.debug('Reading defaults from %r', file_)
            with salt.utils.files.fopen(file_) as fhr:
                defaults = loader(fhr)
                log.debug('Read defaults %r', defaults)
            return defaults or {}