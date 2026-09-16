def load_notebook(resources=None, verbose=False, hide_banner=False,
    load_timeout=5000):
    global _NOTEBOOK_LOADED
    from .. import __version__
    from ..core.templates import NOTEBOOK_LOAD
    from ..util.serialization import make_id
    from ..resources import CDN
    from ..util.compiler import bundle_all_models
    if resources is None:
        resources = CDN
    if not hide_banner:
        if resources.mode == 'inline':
            js_info = 'inline'
            css_info = 'inline'
        else:
            js_info = resources.js_files[0] if len(resources.js_files
                ) == 1 else resources.js_files
            css_info = resources.css_files[0] if len(resources.css_files
                ) == 1 else resources.css_files
        warnings = [('Warning: ' + msg['text']) for msg in resources.
            messages if msg['type'] == 'warn']
        if _NOTEBOOK_LOADED and verbose:
            warnings.append('Warning: BokehJS previously loaded')
        element_id = make_id()
        html = NOTEBOOK_LOAD.render(element_id=element_id, verbose=verbose,
            js_info=js_info, css_info=css_info, bokeh_version=__version__,
            warnings=warnings)
    else:
        element_id = None
    _NOTEBOOK_LOADED = resources
    custom_models_js = bundle_all_models() or ''
    nb_js = _loading_js(resources, element_id, custom_models_js,
        load_timeout, register_mime=True)
    jl_js = _loading_js(resources, element_id, custom_models_js,
        load_timeout, register_mime=False)
    if not hide_banner:
        publish_display_data({'text/html': html})
    publish_display_data({JS_MIME_TYPE: nb_js, LOAD_MIME_TYPE: jl_js})