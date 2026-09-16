def deactivate(profile='default'):
    with jconfig(profile) as config:
        deact = True
        if not getattr(config.NotebookApp.contents_manager_class,
            'startswith', lambda x: False)('jupyterdrive'):
            deact = False
        if 'gdrive' not in getattr(config.NotebookApp.tornado_settings,
            'get', lambda _, __: '')('contents_js_source', ''):
            deact = False
        if deact:
            del config['NotebookApp']['tornado_settings']['contents_js_source']
            del config['NotebookApp']['contents_manager_class']