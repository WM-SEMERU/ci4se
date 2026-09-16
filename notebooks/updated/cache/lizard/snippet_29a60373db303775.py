def get_node_instances(nodelist, instances):
    context = _get_main_context(nodelist)
    if TemplateAdapter is not None and isinstance(nodelist, TemplateAdapter):
        nodelist = nodelist.template
    return _scan_nodes(nodelist, context, instances)