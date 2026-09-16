def resolve_any_xref(self, env, fromdocname, builder, target, node, contnode):
    prefix = node.get('dn:prefix')
    results = []
    match = self.find_obj(env, prefix, target, None, 1)
    if match is not None:
        name, obj = match
        results.append(('dn:' + self.role_for_objtype(obj[1]), make_refnode
            (builder, fromdocname, obj[0], name, contnode, name)))
    return results