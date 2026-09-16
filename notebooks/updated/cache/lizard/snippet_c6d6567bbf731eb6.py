def setup(app):
    sphinx_compatibility._app = app
    app.add_config_value('sphinx_gallery_conf', DEFAULT_GALLERY_CONF, 'html')
    for key in ['plot_gallery', 'abort_on_example_error']:
        app.add_config_value(key, get_default_config_value(key), 'html')
    try:
        app.add_css_file('gallery.css')
    except AttributeError:
        app.add_stylesheet('gallery.css')
    extensions_attr = '_extensions' if hasattr(app, '_extensions'
        ) else 'extensions'
    if 'sphinx.ext.autodoc' in getattr(app, extensions_attr):
        app.connect('autodoc-process-docstring', touch_empty_backreferences)
    app.connect('builder-inited', generate_gallery_rst)
    app.connect('build-finished', copy_binder_files)
    app.connect('build-finished', summarize_failing_examples)
    app.connect('build-finished', embed_code_links)
    metadata = {'parallel_read_safe': True, 'parallel_write_safe': False,
        'version': _sg_version}
    return metadata