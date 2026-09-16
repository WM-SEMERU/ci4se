def _format_config_nodes(self, modulename, classname):
    fullname = '{0}.{1}.config'.format(modulename, classname)
    desc_sig_node = desc_signature()
    desc_sig_node['module'] = modulename
    desc_sig_node['class'] = classname
    desc_sig_node['fullname'] = fullname
    prefix = 'attribute'
    desc_sig_node += desc_annotation(prefix, prefix)
    desc_sig_name_node = desc_addname('config', 'config')
    desc_sig_name_node['classes'].extend(['xref', 'py'])
    desc_sig_node += desc_sig_name_node
    summary_text = 'Access configuration fields and retargetable subtasks.'
    content_node_p = nodes.paragraph(text=summary_text)
    content_node = desc_content()
    content_node += content_node_p
    desc_node = desc()
    desc_node['noindex'] = True
    desc_node['domain'] = 'py'
    desc_node['objtype'] = 'attribute'
    desc_node += desc_sig_node
    desc_node += content_node
    return desc_node