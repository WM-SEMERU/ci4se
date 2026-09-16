def resolve_xref(self, env, fromdocname, builder, type_name, target, node,
    contnode):
    if type_name == 'chplref':
        if node['refexplicit']:
            docname, labelid = self.data['anonlabels'].get(target, ('', ''))
            sectname = node.astext()
        else:
            docname, labelid, sectname = self.data['labels'].get(target, (
                '', '', ''))
        if not docname:
            return None
        return self._make_refnode(fromdocname, builder, docname, labelid,
            sectname, contnode)
    modname = node.get('chpl:module')
    clsname = node.get('chpl:class')
    searchmode = 1 if node.hasattr('refspecific') else 0
    matches = self.find_obj(env, modname, clsname, target, type_name,
        searchmode)
    if not matches:
        return None
    elif len(matches) > 1:
        env.warn_node(
            'more than one target found for cross-reference %r: %s' % (
            target, ', '.join(match[0] for match in matches)), node)
    name, obj = matches[0]
    if obj[1] == 'module':
        return self._make_module_refnode(builder, fromdocname, name, contnode)
    else:
        return make_refnode(builder, fromdocname, obj[0], name, contnode, name)