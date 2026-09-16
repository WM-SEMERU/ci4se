def init_app(self, app):
    if not hasattr(app, 'extensions'):
        app.extensions = {}
    config = app.extensions.setdefault('whooshee', {})
    config['whoosheers_indexes'] = {}
    config['whoosheers'] = self.whoosheers
    config['index_path_root'] = app.config.get('WHOOSHEE_DIR', ''
        ) or 'whooshee'
    config['writer_timeout'] = app.config.get('WHOOSHEE_WRITER_TIMEOUT', 2)
    config['search_string_min_len'] = app.config.get('WHOOSHEE_MIN_STRING_LEN',
        3)
    config['memory_storage'] = app.config.get('WHOOSHEE_MEMORY_STORAGE', False)
    config['enable_indexing'] = app.config.get('WHOOSHEE_ENABLE_INDEXING', True
        )
    if app.config.get('WHOOSHE_MIN_STRING_LEN', None) is not None:
        warnings.warn(WhoosheeDeprecationWarning(
            'The config key WHOOSHE_MIN_STRING_LEN has been renamed to WHOOSHEE_MIN_STRING_LEN. The mispelled config key is deprecated and will be removed in upcoming releases. Change it to WHOOSHEE_MIN_STRING_LEN to suppress this warning'
            ))
        config['search_string_min_len'] = app.config.get(
            'WHOOSHE_MIN_STRING_LEN')
    if not os.path.exists(config['index_path_root']):
        os.makedirs(config['index_path_root'])