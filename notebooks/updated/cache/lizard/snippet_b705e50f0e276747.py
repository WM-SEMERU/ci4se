def _make_gh_link_node(app, rawtext, role, kind, api_type, id, options=None):
    url = '%s/%s/%s' % (_BOKEH_GH, api_type, id)
    options = options or {}
    set_classes(options)
    node = nodes.reference(rawtext, kind + utils.unescape(id), refuri=url,
        **options)
    return node